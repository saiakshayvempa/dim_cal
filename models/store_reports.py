import shutil
import os
from datetime import datetime

def move_files(source_folder, destination_folder):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        return

    # Check if the destination folder exists, if not create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get a list of files in the source folder
    files = os.listdir(source_folder)

    # Move each file from the source folder to the destination folder
    for file in files:
        source_file_path = os.path.join(source_folder, file)
        # Append timestamp to the filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename, extension = os.path.splitext(file)
        new_filename = f"{filename}_{timestamp}{extension}"
        destination_file_path = os.path.join(destination_folder, new_filename)
        shutil.move(source_file_path, destination_file_path)


# # Example usage
# source_folder = "source_folder"
# destination_folder = "destination_folder"
# move_files(source_folder, destination_folder)
