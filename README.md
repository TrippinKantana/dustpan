## dustpan

Dustpan is a simple Python script designed to help keep your Downloads folder tidy by automatically moving files to the Recycle Bin. This script can be especially useful for users who frequently download files but forget to clean up their Downloads folder afterward.

## Features
Automatic Cleanup: Dustpan scans your Downloads folder and moves files to the Recycle Bin, freeing up space and keeping your Downloads folder organized.
Customizable: You can easily customize which file types Dustpan should clean up by modifying the list of allowed file extensions in the script.
Cross-Platform: Dustpan is compatible with Windows, macOS, and Linux, allowing users on different operating systems to benefit from its cleanup functionality.

## How to Use
Clone the Dustpan repository to your local machine using the following command
git clone https://github.com/trippinkantana/dustpan.git

Change your current directory to the Dustpan directory
cd dustpan

Run the Script
dustpan.py

Dustpan will scan your Downloads folder and move files with allowed file extensions to the Recycle Bin. Once the cleanup is complete, you'll see a message indicating that the cleanup is finished.
Customization
You can customize Dustpan to fit your needs by modifying the list of allowed file extensions in the dustpanlimited.py script. By default, Dustpan is configured to clean up files with the following extensions:

.png
.jpg
.zip
.mp3
.apk

You can add or remove file extensions from this list according to your preferences.

## Contributions
Contributions to Dustpan are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the GitHub repository.

## License
Dustpan is licensed under the MIT License. See the LICENSE file for more details.

## Disclaimer
Dustpan is provided as-is without any warranty. Use it at your own risk. The author is not responsible for any loss of data or damage caused by the use of Dustpan.

## Acknowledgments
Dustpan uses the send2trash library to move files to the Recycle Bin. Special thanks to the developers of send2trash for their contribution to the project.
