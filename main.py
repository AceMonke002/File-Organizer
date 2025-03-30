import os
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def organize_files():
    folder_path = filedialog.askdirectory()
    if not folder_path:  
        return  

    folder_variable.set(folder_path)  
    before_listbox.delete(0, tk.END)
    after_listbox.delete(0, tk.END)

    try:
        files = os.listdir(folder_path)  
        for file in files:
            before_listbox.insert(tk.END, file)
        
        for file in files:
            file_path = os.path.join(folder_path, file)  
            if os.path.isfile(file_path):  
                ext = os.path.splitext(file)[1][1:]  
                if ext:  
                    target_folder = os.path.join(folder_path, ext)
                    os.makedirs(target_folder, exist_ok=True)  
                    shutil.move(file_path, os.path.join(target_folder, file)) 
        sorted_files = []
        for root_dir, _, files in os.walk(folder_path):  
            for file in files:
                sorted_files.append(os.path.relpath(os.path.join(root_dir, file), folder_path))

        for sorted_file in sorted_files:
            after_listbox.insert(tk.END, sorted_file)

        messagebox.showinfo("PlaceHolder","Files Sorted!") 

    except Exception as e:
        print(f"Error processing folder: {e}")


root = tk.Tk()
root.title("File Organizer")
root.geometry('600x400')
root.resizable(False, False)

folder_variable = tk.StringVar()

title_label = tk.Label(root, text="Select a folder to sort its files")
title_label.pack(pady=5)

select_button = tk.Button(root, text="Select Folder", command=organize_files)
select_button.pack(pady=5)

label = tk.Label(root, textvariable=folder_variable)
label.pack(pady=10)

listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)

before_label = tk.Label(listbox_frame, text="Before Sorting")
before_label.grid(row=0, column=0, padx=10)

before_listbox = tk.Listbox(listbox_frame, width=40, height=15)
before_listbox.grid(row=1, column=0, padx=10)

after_label = tk.Label(listbox_frame, text="After Sorting")
after_label.grid(row=0, column=1, padx=10)

after_listbox = tk.Listbox(listbox_frame, width=40, height=15)
after_listbox.grid(row=1, column=1, padx=10)

root.mainloop()
