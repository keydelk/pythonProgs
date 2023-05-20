import tkinter as tk
from tkinter import messagebox

def return_pressed(event):
    value = entry.get()
    messagebox.showinfo(
        title="Enter Pressed",
        message=f"Name: {value}"
        )

window = tk.Tk()

label = tk.Label(text="Name")
entry = tk.Entry()
label.pack()
entry.pack()

window.bind("<Return>", return_pressed)