import os
import shutil

# Set the source and destination directories
src_dir = "C:\\Users\\Khushnood Asif\\Downloads"
dst_dir = "D:\\Files\\1. Applications"

# Make sure the destination directory exists
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

# Walk through the source directory
for root, dirs, files in os.walk(src_dir):
    for file in files:
        # Check if the file is a zip file
        if file.endswith(".zip"):
            # Construct the full path to the file
            src_path = os.path.join(root, file)
            dst_path = os.path.join(dst_dir, file)
            # Move the file
            shutil.move(src_path, dst_path)

print("Finished moving zip files.")
