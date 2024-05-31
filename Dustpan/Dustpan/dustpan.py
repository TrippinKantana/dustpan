import os
from send2trash import send2trash

# Specify the path to your Downloads folder
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# List all files in the Downloads folder
files = os.listdir(downloads_folder)

# Move each file to the Recycle Bin
for file in files:
    file_path = os.path.join(downloads_folder, file)
    if os.path.isfile(file_path):
        send2trash(file_path)
        print(f"Moved {file} to Recycle Bin.")

print("Cleanup completed.")

