"""
Automatic Git Synchronization for codealpha_automation (Task 3)
Continuously monitors local project files for changes, stages them,
generates a descriptive commit message, and pushes to origin main.

Safety guarantees:
- Never uses git push --force.
- Never resets, deletes, or moves files.
- Never modifies move_jpg.py.
- Displays changed files and commit message before pushing.
"""

import os
import sys
import time
import subprocess
from datetime import datetime
from pathlib import Path

# Project root directory
PROJECT_DIR = Path(__file__).resolve().parent
BRANCH = "main"
REMOTE = "origin"
POLL_INTERVAL = 5  # seconds
DEBOUNCE_WAIT = 2  # seconds after change detection to let writes complete


def run_git_command(args, check=True):
    """Executes a git command in the project directory."""
    result = subprocess.run(
        ["git"] + args,
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )
    if check and result.returncode != 0:
        raise RuntimeError(
            f"Git command failed: git {' '.join(args)}\nError: {result.stderr.strip()}"
        )
    return result


def get_git_changes():
    """Returns a list of (action, filename) from git status --porcelain."""
    result = run_git_command(["status", "--porcelain"])
    lines = [line for line in result.stdout.splitlines() if line.strip()]
    if not lines:
        return []

    changes = []
    for line in lines:
        code = line[:2]
        filename = line[3:].strip()
        if filename.startswith('"') and filename.endswith('"'):
            filename = filename[1:-1]

        if "?" in code:
            action = "Added"
        elif "D" in code:
            action = "Deleted"
        elif "M" in code:
            action = "Modified"
        elif "A" in code:
            action = "Added"
        elif "R" in code:
            action = "Renamed"
        else:
            action = "Changed"
        changes.append((action, filename))
    return changes


def generate_commit_message(changes):
    """Creates a descriptive commit message based on detected changes."""
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if len(changes) == 1:
        action, fname = changes[0]
        summary = f"{action.lower()} {fname}"
    elif len(changes) <= 3:
        summary = ", ".join(f"{action.lower()} {fname}" for action, fname in changes)
    else:
        summary = f"update {len(changes)} files ({changes[0][1]}, {changes[1][1]}, ...)"
    return f"Auto-sync ({now_str}): {summary}"


def sync_cycle():
    """Performs one check and sync cycle if changes are detected."""
    changes = get_git_changes()
    if not changes:
        return False

    # Debounce wait to let multi-file saves finish
    time.sleep(DEBOUNCE_WAIT)
    # Re-check after debounce
    changes = get_git_changes()
    if not changes:
        return False

    commit_msg = generate_commit_message(changes)

    print("\n" + "=" * 65)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Detected {len(changes)} file change(s):")
    for action, fname in changes:
        print(f"   - {action:10s} : {fname}")
    print(f"\n[Generated Commit Message]:")
    print(f"   \"{commit_msg}\"")
    print("=" * 65)

    # 1. Stage changes
    print("-> Staging files with 'git add -A'...")
    run_git_command(["add", "-A"])

    # 2. Commit changes
    print("-> Committing changes...")
    commit_res = run_git_command(["commit", "-m", commit_msg], check=False)
    if commit_res.returncode != 0:
        print(f"[!] Commit skipped: {commit_res.stdout.strip() or commit_res.stderr.strip()}")
        return False

    # 3. Push to remote main (strictly without --force)
    print(f"-> Pushing to {REMOTE} {BRANCH} (safe fast-forward, no force)...")
    push_res = run_git_command(["push", REMOTE, BRANCH], check=False)
    if push_res.returncode == 0:
        print("[SUCCESS] Successfully synchronized with GitHub repository!")
        print(push_res.stderr.strip() or push_res.stdout.strip())
    else:
        print(f"[ERROR] Push failed:\n{push_res.stderr.strip()}")

    print("-" * 65 + "\n")
    return True


def watch_and_sync():
    """Continuously monitors the repository and triggers sync on changes."""
    print("=" * 65)
    print("  codealpha_automation - Auto Git Sync Service")
    print(f"  Watching: {PROJECT_DIR}")
    print(f"  Target:   {REMOTE}/{BRANCH}")
    print(f"  Check interval: {POLL_INTERVAL} seconds")
    print("  Press Ctrl+C to stop.")
    print("=" * 65 + "\n")

    try:
        while True:
            try:
                sync_cycle()
            except Exception as e:
                print(f"[!] Error during sync cycle: {e}")
            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        print("\n[STOPPED] Auto Git Sync stopped by user.")


if __name__ == "__main__":
    if "--once" in sys.argv:
        print(f"Running single sync check for {PROJECT_DIR}...")
        performed = sync_cycle()
        if not performed:
            print("Working tree is clean. No changes detected.")
    else:
        watch_and_sync()
