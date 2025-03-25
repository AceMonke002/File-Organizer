import os
import pathlib
from pathlib import Path
import shutil

def sort_files(dir):
    dir = Path(dir)
    for file in os.listdir(dir):  # Loop through all files in the given directory
        file_path = dir / file  # Construct full path to the file
        
        if file_path.is_file():  # Ensure it's a file
            ext = file_path.suffix[1:]  # Get file extension removing the dot
            
            if ext:  # Skip files with no extensions
                target_folder = dir / ext  # Create a target folder named after the file extension
                
                target_folder.mkdir(exist_ok=True)  # Create the folder if it doesn’t exist
                
                shutil.move(str(file_path), str(target_folder / file))  # Move the file into its corresponding folder


def main():
    loop_variable = False
    while not loop_variable:
        path = Path(input('Please input the folder path youd like to sort: '))
        if path.exists():
            sort_files(path)
            print('Files Sorted')
            loop_variable = True
        else:
            print('Path does not exist, try again')

main()
