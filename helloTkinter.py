#!/usr/bin/env python3

import tkinter
from tkinter import ttk

window = tkinter.Tk()
frame = ttk.Frame(window, padding = 10)
frame.grid()
helloLabel = ttk.Label(frame, text="Hello Tkinter").grid(column=0, row=0)

button = ttk.Button(frame, text="Quit", command=window.destroy).grid(column=1, row=0)

window.mainloop()
