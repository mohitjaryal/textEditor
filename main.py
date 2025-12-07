# Text Editor using Pyhton

import tkinter as tk
from tkinter import filedialog, messagebox


def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename (defaultextension='.txt',filetypes=[('Text Files','*.txt')])
    if file_path:
        with open(file_path)