import tkinter as tk
from tkinter import ttk

window = tk.Tk()

message = tk.Label(
    text="Hello, Tkinter",
    fg="black",
    bg="#626DAD"
    )
message.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="#dad626"
    )

button.pack()

window.mainloop()