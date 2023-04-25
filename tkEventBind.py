import tkinter as tk

window = tk.Tk()

# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

# button click event
def handle_click(event):
    print("The button was clicked!")

# create the button
button = tk.Button(text="Click Me")
button.bind("<Button-1>", handle_click)
button.pack()

# Run the event loop
window.mainloop()