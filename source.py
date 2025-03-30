import os
import shutil
import argparse

def organize_files(folder_path):

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".avi", ".mov", ".mkv"],
        "Music": [".mp3", ".wav", ".aac", ".flac"],
        "Archives": [".zip", ".rar", ".tar", ".gz"]
    }
    
    if not os.path.exists(folder_path):
        print("Error: The specified folder does not exist.")
        return
    
    # Iterate through all files in the folder
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)  # Get the full file path
        if os.path.isfile(file_path):  # Ensure it's a file and not a directory
            for category, extensions in file_types.items():  # Loop through file types
                if file.lower().endswith(tuple(extensions)):  # Check file extension
                    category_folder = os.path.join(folder_path, category)  # Define category folder path
                    os.makedirs(category_folder, exist_ok=True)  # Create category folder if it doesn't exist
                    shutil.move(file_path, os.path.join(category_folder, file))  # Move file to category folder
                    break  # Stop checking once a match is found
    
    print("Files have been organized successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize files in a folder by category.")
    parser.add_argument("folder", help="Path to the folder to organize")
    args = parser.parse_args()
    
    organize_files(args.folder)
