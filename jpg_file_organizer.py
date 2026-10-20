
import os
import shutil

# Source and destination folders
source_folder = "source_images"
destination_folder = "organized_images"

# Check whether the source folder exists
if not os.path.isdir(source_folder):
    print("Error: Source folder does not exist.")
else:
    # Create destination folder if needed
    os.makedirs(destination_folder, exist_ok=True)

    moved_count = 0

    # Find and move JPG files
    for filename in os.listdir(source_folder):
        if filename.lower().endswith((".jpg", ".jpeg")):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(
                destination_folder, filename
            )

            # Avoid overwriting an existing file
            if os.path.exists(destination_path):
                print(f"Skipped {filename}: already exists.")
                continue

            shutil.move(source_path, destination_path)
            print(f"Moved: {filename}")
            moved_count += 1

    print(f"\nFinished! Total JPG files moved: {moved_count}")
