# Text Editor using Pyhton

import tkinter as tk
from tkinter import filedialog, messagebox

# for making new file
def new_file():
    text.delete(1.0, tk.END)

# for opening file
def open_file():
    file_path = filedialog.askopenfilename (defaultextension='.txt',filetypes=[('Text Files','*.txt')])
    if file_path:
        with open(file_path,'r'):
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

# for save file
def save_file():
    file_path = filedialog.askopenfilename(defaultextension='.txt',filetypes=[('Text Files','*.txt')])
    if file_path:
        with open(file_path,'w') as file:
            file.write(text.get(1.0,tk.END))
            messagebox.showinfo('Info', 'File saved Successfully')


root = tk.Tk()
root.title('VrtX')
root.geometry('800x600')

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
