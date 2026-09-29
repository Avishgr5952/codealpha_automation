import os
import shutil

# Step 1: Define source and destination folder paths
SOURCE_DIR = "source"
DEST_DIR = "destination"

def move_jpg_files():
    """
    Scans the source folder, finds all .jpg files, 
    and moves them to the destination folder using os and shutil.
    """
    # Check if the source folder exists
    if not os.path.exists(SOURCE_DIR):
        print(f"Error: The source folder '{SOURCE_DIR}' does not exist.")
        return

    # Ensure the destination folder exists; create it if missing
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
        print(f"Created destination folder: '{DEST_DIR}'")

    # Counter to keep track of how many files are moved
    moved_count = 0

    # Get a list of all file and folder names inside the source directory
    file_list = os.listdir(SOURCE_DIR)

    print("--- Starting File Automation ---")

    # Loop through each file in the source directory
    for filename in file_list:
        # Construct the complete path to the file in the source folder
        source_path = os.path.join(SOURCE_DIR, filename)

        # Verify that it is a file and ends with .jpg (case-insensitive)
        if os.path.isfile(source_path) and filename.lower().endswith(".jpg"):
            # Construct the destination path
            dest_path = os.path.join(DEST_DIR, filename)

            try:
                # Move the file using shutil.move()
                shutil.move(source_path, dest_path)
                print(f"[MOVED]   {filename} -> {DEST_DIR}/")
                moved_count += 1
            except Exception as e:
                # Handle any unexpected error (e.g., permissions, locked files)
                print(f"[ERROR]   Failed to move {filename}. Reason: {e}")
        else:
            # Leave non-jpg files untouched
            print(f"[SKIPPED] {filename} (not a .jpg file)")

    print("--------------------------------")
    print(f"Automation Complete! Total .jpg files moved: {moved_count}\n")

if __name__ == "__main__":
    move_jpg_files()
