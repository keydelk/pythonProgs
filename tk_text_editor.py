#!/usr/bin/env python3

"""A simple text editor made with tkinter."""
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

NUMBER = 0

def evaluate_text():
    """Evaluate the text and return the result in an alert"""
    global NUMBER
    NUMBER = NUMBER + 1
    text = txt_edit.get("1.0", tk.END)
    try:
        if text.strip() == "9+10":
            result = 21
        else:
            result = eval(text)
        tk.messagebox.showinfo(
            title="Evaluation Results {}".format(NUMBER),
            message="Result is: {}".format(result)
            )
    except:
        tk.messagebox.showerror(
            title="Evaluation Error",
            message="Invalid expression"
            )

def validate_parentheses():
    """ Validate that all parentheses are correctly matched"""
    # define which characters are used as parentheses and
    # which closeing parentheses go with which open parentheses
    parens = {')': '(', ']': '[', '}': '{'}
    # store opening parens in a stack
    parenstack = []
    # store text so we're not constantly calling the get method
    text = txt_edit.get("1.0", tk.END)
    # check each character in the text
    for c in text:
        # if c is an opening paren, push it on the stack
        if c in parens.values():
            parenstack.append(c)
        # if c is a closing paren, check that its match is on top
        elif c in parens.keys():
            # if not a match, tell the user
            if not parenstack or parens[c] != parenstack[-1]:
                tk.messagebox.showwarning(
                    title="Parentheses Validation",
                    message=f"Unmatched closing parentheses {c}"
                    )
                return
            # else pop the match off the stack
            else:
                parenstack.pop()
        # no need for a final else statement, since we just ignore other characters
        # and continue to the next iteration
    # After checking all the text, if there are any parentheses in the stack,
    # they are missing their match
    if not parenstack:
        tk.messagebox.showinfo(
            title="Parentheses Validation",
            message="Parentheses are valid."
            )
        return()
    else:
        tk.messagebox.showwarning(
            title="Parentheses Validation",
            message=f"Unmatched opening parentheses {parenstack[-1]}"
            )

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Tk Text Editor - {filepath}")


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Tk Text Editor - {filepath}")

window = tk.Tk()
window.title("Tk Text Editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file)
btn_validate_parens = tk.Button(frm_buttons,
                                text="Check Parentheses",
                                command=validate_parentheses)
btn_evaluate = tk.Button(frm_buttons, text="Evaluate", command=evaluate_text)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_validate_parens.grid(row=2, column=0, sticky="ew", padx=5,pady=5)
btn_evaluate.grid(row=3, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
