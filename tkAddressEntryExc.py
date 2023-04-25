import tkinter as tk

# Create a new window with the title "Address Entry Form"
window = tk.Tk()
window.title("Address Entry Form")

# Create a new frame 'frm_form' to contain the label
# and entry widgets for entering address information.
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

# List of field labels
fields = ["First Name:",
          "Last Name:",
          "Address Line 1:",
          "Address Line 2:",
          "City:",
          "State/Province:",
          "Postal Code:",
          "Country:"
          ]

# Loop over fields to create the form
for idx, field in enumerate(fields):
    lbl = tk.Label(master=frm_form, text=field)
    ent = tk.Entry(master=frm_form, width=50)
    lbl.grid(row=idx, column=0, sticky="e")
    ent.grid(row=idx, column=1, sticky="w")

# Create a frame for the buttons
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

btn_clear = tk.Button(master=frm_buttons, text="Clear")
btn_clear.pack(side=tk.RIGHT, ipadx=10)


window.mainloop()