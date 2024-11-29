import os
import shutil
import json
import logging

# Set up logging
logging.basicConfig(
    filename="logs/organization.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_config():
    """Load file type mappings from config.json."""
    with open("config.json", "r") as config_file:
        return json.load(config_file)

def organize_files(directory, file_types):
    """Organize files in the given directory based on file type mappings."""
    if not os.path.exists(directory):
        return "Directory does not exist."

    # Create subfolders for file types
    for folder_name in file_types.keys():
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files
    moved_files = 0
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            moved = False
            for folder_name, extensions in file_types.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, folder_name, file))
                    logging.info(f"Moved: {file} -> {folder_name}")
                    moved = True
                    moved_files += 1
                    break
            if not moved:
                # Move to 'Others' if no match
                shutil.move(file_path, os.path.join(directory, "Others", file))
                logging.info(f"Moved: {file} -> Others")
                moved_files += 1

    return f"Organized {moved_files} files."

