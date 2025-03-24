import os
import pathlib
from pathlib import Path
import shutil

path = Path(input('Please input the folder path youd like to sort: '))
print(path.exists())
files = os.listdir(path)
print(files)
for file in os.listdir(path):
    file_path = Path(file)
    file_extension = file_path.suffix
    print(file_extension)

def create_folder(directory, folder_name):
    folder_path = os.path.join(directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)

create_folder("test", "test1")

source =''
destination = ''
shutil.move(source, destination)