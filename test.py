import tkinter as tk
from tkinter import filedialog
import os

def select_folder():
    folder_path = filedialog.askdirectory()  # Opens a folder selection dialog
    if folder_path:  # Check if the user selected a folder
        folder_variable.set(folder_path)  # Store the folder path in a Tkinter variable
        list_files(folder_path)  # List the files in the selected folder

def list_files(folder_path):
    # Get the list of files in the folder
    try:
        files = os.listdir(folder_path)  # List all files and folders in the directory
        files_listbox.delete(0, tk.END)  # Clear the current list
        for file in files:
            files_listbox.insert(tk.END, file)  # Add files to the listbox
    except Exception as e:
        print(f"Error reading folder: {e}")

root = tk.Tk()
root.title("Folder and Files Selector")

# Create a variable to store the folder path
folder_variable = tk.StringVar()

# Create a button that triggers the folder selection
button = tk.Button(root, text="Select Folder", command=select_folder)
button.pack(pady=20)

# Label to display the selected folder path
label = tk.Label(root, textvariable=folder_variable)
label.pack(pady=10)

# Listbox to display the files in the selected folder
files_listbox = tk.Listbox(root, width=50, height=10)
files_listbox.pack(pady=10)

root.mainloop()
