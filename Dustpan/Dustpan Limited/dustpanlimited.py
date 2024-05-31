import os
from send2trash import send2trash

# Specify the path to your Downloads folder
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# List all files in the Downloads folder
files = os.listdir(downloads_folder)

# Specify the file extensions you want to move to the Recycle Bin
allowed_extensions = ['.png', '.jpg', '.zip', '.mp3', '.apk' ]

# Move files with allowed extensions to the Recycle Bin
for file in files:
    file_path = os.path.join(downloads_folder, file)
    if os.path.isfile(file_path) and any(file.lower().endswith(ext) for ext in allowed_extensions):
        send2trash(file_path)
        print(f"Moved {file} to Recycle Bin.")

print("Cleanup completed.")
