# Task 3: Task Automation with Python Scripts

## 1. Title
**File Organizer Automation: Automated JPG Image Sorter**

---

## 2. Objective
The primary objective of this project is to automate a repetitive file management task using Python. Specifically, the script scans a source folder containing heterogeneous files, filters out only files with the `.jpg` extension, and automatically transfers them to a designated destination folder while preserving all other files and folder structure.

---

## 3. Problem Statement
In day-to-day computer usage, files such as images, documents, screenshots, and text files often accumulate in a single directory (e.g., Downloads, Desktop, or Camera imports). Manually filtering, selecting, and moving specific image files (such as `.jpg` images) into dedicated storage folders is:
- **Time-consuming:** Users must manually select multiple individual files.
- **Error-prone:** Users risk accidentally moving, skipping, or deleting unrelated files (such as `.png` images or `.txt` documents).
- **Repetitive:** Doing this on a regular basis wastes productivity.

An automated Python script solves this problem by performing the detection, verification, and file transfer in seconds without requiring manual intervention.

---

## 4. Tools and Technologies
- **Programming Language:** Python 3.x
- **Development Environment:** Visual Studio Code (VS Code) / Terminal
- **Built-in Modules:**
  - `os`: Used for directory inspection, verifying file existence, checking item types, and constructing cross-platform file paths.
  - `shutil`: Used for high-level file system operations, specifically moving files between directories (`shutil.move()`).
- **External Dependencies:** None (Relies strictly on Python standard library modules).

---

## 5. Project Structure
```text
automation/
│
├── move_jpg.py         # Main Python automation script
├── TASK3_REPORT.md     # Comprehensive project report & assessment documentation
├── TASK3_README.md     # Quick-start instructions for running the project
│
├── source/             # Source directory containing mixed files
│   ├── document.txt    # Non-JPG file (persists in source)
│   └── photo.png       # Non-JPG file (persists in source)
│
└── destination/        # Destination directory for sorted files
    ├── image1.jpg      # Moved JPG image
    ├── image2.jpg      # Moved JPG image
    └── image3.jpg      # Moved JPG image
```

---

## 6. Description
The project consists of a Python automation script named `move_jpg.py` that interacts directly with the local file system. 

1. **Path Configuration:** The script defines constants `SOURCE_DIR = "source"` and `DEST_DIR = "destination"`.
2. **Directory Validation:** Before processing, it ensures the source folder exists. If the destination folder does not already exist, it creates it automatically using `os.makedirs()`.
3. **Directory Scanning:** The script reads all item names inside the source directory with `os.listdir()`.
4. **Conditional Filtering:** For each item, the script combines the folder and file name using `os.path.join()`, verifies that the item is a regular file (`os.path.isfile()`), and checks whether the filename ends with `.jpg` (in a case-insensitive manner using `.lower().endswith(".jpg")`).
5. **Safe File Relocation:** If a file matches the criteria, `shutil.move()` relocates the file to the destination folder inside a `try...except` block to gracefully catch potential I/O or permission errors.
6. **Detailed Reporting:** The console displays real-time feedback for every item scanned (`[MOVED]` or `[SKIPPED]`), culminating in a final summary count of all moved files.

---

## 7. Algorithm
1. **Start** the automation program.
2. **Define folder paths**: Set `SOURCE_DIR` to `"source"` and `DEST_DIR` to `"destination"`.
3. **Check Source Directory**:
   - If `source` folder does not exist, display an error message and terminate the script.
4. **Check Destination Directory**:
   - If `destination` folder does not exist, create it.
5. **Initialize Counter**: Set `moved_count = 0`.
6. **Read Directory Items**: Retrieve the list of all filenames in `SOURCE_DIR` using `os.listdir()`.
7. **Iterate Through Items**: For each `filename` in the list:
   - Form the complete file path: `source_path = os.path.join(SOURCE_DIR, filename)`.
   - **Condition Check**: Check if `os.path.isfile(source_path)` is True AND `filename.lower().endswith(".jpg")` is True.
     - **If True**:
       - Form destination path: `dest_path = os.path.join(DEST_DIR, filename)`.
       - Execute `shutil.move(source_path, dest_path)` inside a `try...except` block.
       - If successful, print `[MOVED]` notification and increment `moved_count` by 1.
       - If an error occurs, catch the exception and print an error message.
     - **If False**:
       - Print `[SKIPPED]` notification indicating the item is not a `.jpg` file.
8. **Summary**: Print the completion banner and display the total number of files moved (`moved_count`).
9. **End** the automation program.

---

## 8. Python Code (`move_jpg.py`)
Below is the full, unabridged source code for `move_jpg.py`:

```python
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
```

---

## 9. Testing

### Initial State Before Execution
- **`source/` folder contents:**
  - `image1.jpg`
  - `image2.jpg`
  - `photo.png`
  - `document.txt`
  - `image3.jpg`
- **`destination/` folder contents:**
  - Empty

### Execution Steps
1. Open terminal in the project root directory (`C:\Users\avish\OneDrive\Desktop\automation`).
2. Run the script for the first time:
   ```bash
   python move_jpg.py
   ```
3. Run the script for a second time to verify idempotency (handling folders where target files have already been processed):
   ```bash
   python move_jpg.py
   ```

---

## 10. Actual Test Result

### Execution 1: First Run (Initial Transfer)
During the first run, the script processed all 5 items, identified the 3 `.jpg` files, and successfully transferred them to `destination/`. Non-JPG files remained in `source/`.

**Terminal Output:**
```text
--- Starting File Automation ---
[SKIPPED] document.txt (not a .jpg file)
[MOVED]   image1.jpg -> destination/
[MOVED]   image2.jpg -> destination/
[MOVED]   image3.jpg -> destination/
[SKIPPED] photo.png (not a .jpg file)
--------------------------------
Automation Complete! Total .jpg files moved: 3
```

### Execution 2: Second Run (Subsequent Check)
During the second run, all `.jpg` files were already located in `destination/`. The script evaluated the remaining files in `source/` (`document.txt` and `photo.png`), correctly recognized that neither was a `.jpg` file, and safely completed moving 0 files without errors.

**Terminal Output:**
```text
--- Starting File Automation ---
[SKIPPED] document.txt (not a .jpg file)
[SKIPPED] photo.png (not a .jpg file)
--------------------------------
Automation Complete! Total .jpg files moved: 0
```

### Final Folder State Verification
- **`source/` contents:**
  - `document.txt`
  - `photo.png`
- **`destination/` contents:**
  - `image1.jpg`
  - `image2.jpg`
  - `image3.jpg`

---

## 11. Real-Life Application
This automation pattern has numerous practical applications in enterprise and personal productivity workflows:
1. **Automated Photo Organization:** Automatically sorting SD card camera dumps or smartphone imports by format (`.jpg`, `.raw`, `.mp4`).
2. **Downloads Folder Cleaner:** Periodically sorting cluttered download directories by routing PDFs to a `Documents/` folder, installers to an `Installers/` folder, and images to a `Pictures/` folder.
3. **Data Preprocessing Pipelines:** In machine learning workflows, pre-sorting raw image datasets based on file extensions before data ingestion.
4. **Scheduled Background Tasks:** Integrating this script with Windows Task Scheduler or a cron job to automatically organize folders on a daily or hourly basis.

---

## 12. Conclusion
The "Move all .jpg files from a folder to a new folder" task successfully illustrates the power and simplicity of Python for system automation. By utilizing standard built-in modules (`os` and `shutil`), the script provides:
- Clean and readable logic suitable for beginners.
- Robust error handling and condition validation.
- Complete safety for non-target files.
- Repeatable, predictable execution without any external dependencies.

---

## 13. Viva Questions and Answers

### Q1: What is the role of the `os` module in this script?
**Answer:** The `os` module provides an interface to interact with the host operating system. In this project, it is used for:
- Checking whether directories exist (`os.path.exists()`).
- Creating missing directories safely (`os.makedirs()`).
- Listing the files and folders inside a directory (`os.listdir()`).
- Building clean, platform-independent file path strings (`os.path.join()`).
- Verifying whether an item is a file rather than a subdirectory (`os.path.isfile()`).

### Q2: What is the role of the `shutil` module and how does it differ from `os`?
**Answer:** While `os` is primarily used for path handling, file metadata, and environment management, `shutil` (Shell Utilities) provides high-level file operations. We use `shutil.move(src, dst)` to relocate files from one folder to another in a single operation, akin to a cut-and-paste action.

### Q3: How does the script identify `.jpg` files?
**Answer:** The script checks two conditions:
1. It uses `os.path.isfile(source_path)` to ensure the target item is a file and not a directory.
2. It uses `filename.lower().endswith(".jpg")`. The `.lower()` method normalizes the filename so uppercase extensions like `.JPG` or `.Jpg` are matched reliably, and `.endswith(".jpg")` checks the file extension.

### Q4: Why did the second execution move 0 files?
**Answer:** Because `shutil.move()` moves the files rather than copying them. Once the first execution finished, the JPG files were physically relocated to the destination folder. During the second run, only `document.txt` and `photo.png` remained in the source directory; both were skipped because neither is a `.jpg` file.

### Q5: What error handling has been included in the script?
**Answer:**
- Directory existence verification prevents runtime errors if the source directory is absent.
- Automatic creation of the destination folder prevents crashes if the folder has not yet been created.
- A `try...except` block wraps the `shutil.move()` call to catch potential permission errors, read-only file locks, or unexpected OS exceptions without stopping the script from processing the remaining files.
