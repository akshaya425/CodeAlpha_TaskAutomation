# CodeAlpha Task Automation — JPG File Organizer

## Project Overview
A Python automation script that moves JPG and JPEG images from a source folder into a destination folder.

## Features
- Identifies `.jpg` and `.jpeg` files
- Automatically moves matching images
- Creates the destination folder if it does not exist
- Skips files with duplicate names to avoid overwriting
- Displays the number of files moved

## Technologies Used
- Python
- `os` module
- `shutil` module

## Project Structure

```text
CodeAlpha_TaskAutomation/
├── jpg_file_organizer.py
├── source_images/
└── organized_images/
```

## How to Run
1. Install Python.
2. Create a folder named `source_images`.
3. Place sample JPG or JPEG images inside it.
4. Open a terminal in the project directory.
5. Run:

   `python jpg_file_organizer.py`

The script moves the matching images into `organized_images`.

## Internship
CodeAlpha Python Programming Internship — Task 3
