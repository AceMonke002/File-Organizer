import os
import pathlib
from pathlib import Path
import shutil
import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Organizer")
        self.geometry("300x450")
        self.resizable(False, False)

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (main, ):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(main)

    def show_frame(self, screen):
        frame = self.frames[screen]
        frame.tkraise()

class main(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        container = tk.Frame(self)
        container.grid(row=0, column=0)

        label = tk.Label(self, text="hey", font=("Arial", 16), anchor="center")
        label.grid(row=0, column=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()