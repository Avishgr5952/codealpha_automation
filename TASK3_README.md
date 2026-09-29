# Task 3: Python Automation Project - Quick Start Guide

## Project: Move All .JPG Files to Destination Folder

This project demonstrates task automation in Python using only standard, built-in modules (`os` and `shutil`). It scans a `source/` folder, identifies all `.jpg` files, and automatically moves them to a `destination/` folder, leaving all other file types untouched.

---

## Prerequisites
- Python 3.x installed on your computer.
- No third-party packages or pip installations required.

---

## How to Run the Project

1. Open your terminal or Visual Studio Code (VS Code).
2. Navigate to the project directory:
   ```bash
   cd C:\Users\avish\OneDrive\Desktop\automation
   ```
3. Run the automation script:
   ```bash
   python move_jpg.py
   ```

---

## Folder Structure
```text
automation/
│
├── move_jpg.py         # Main automation script
├── TASK3_REPORT.md     # Detailed assessment report & viva answers
├── TASK3_README.md     # Instructions and guide
├── source/             # Source directory (non-JPG files remain here)
└── destination/        # Destination directory (moved JPG files)
```

---

## Output Behavior
- **First Run:** Moves all detected `.jpg` files from `source/` to `destination/` and outputs a confirmation message for each file moved.
- **Subsequent Runs:** If all `.jpg` files are already moved, the script safely reports that 0 files were moved, without causing errors or modifying non-JPG files.
