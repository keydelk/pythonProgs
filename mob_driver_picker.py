#!/usr/bin/env python3
# App to pick the next driver for our Python study mob
# Built with the tkinter GUI framework
# Author: Keith Keydel
# Mob Driver Picker © 2024 by Keith Keydel is licensed under CC BY 4.0 
# https://creativecommons.org/licenses/by/4.0/

import tkinter as tk
from tkinter import messagebox
import random

PARTICIPANTS_LABEL = "Participants - Enter participants names, one per line."
ELIGIBLE_PARTICIPANTS_LABEL = "Participants who are 'up' for being picked.\n" \
                              "If empty, this will automatically be populated " \
                              "from the participants list.\n" \
                              "Can manually edit so someone can skip a turn " \
                              "or be put back in."
LICENSE_MESSAGE = "Mob Driver Picker © 2024 by Keith Keydel is licensed under CC BY 4.0\n" \
                  "https://creativecommons.org/licenses/by/4.0/"

def choose_driver(*args):
    """Choose a driver randomly from list of eligible participants
       then remove the participant from the list. When the list
       is empty, refill it from list of participants"""

    # if the eligible participants field is blank, copy over participants
    if not txt_eligible_participants.get("1.0", tk.END).strip():
        txt_eligible_participants.insert(tk.END, txt_participants.get("1.0", tk.END))

    # read the contents of the eligible participant textbox into a list
    # split substrings on new lines
    eligible_participants = txt_eligible_participants.get("1.0", tk.END).strip().split(sep='\n')

    # randomly choose a participant to be the next driver
    driver = random.choice(eligible_participants)
    messagebox.showinfo(
        title="Next Driver",
        message=f"Next driver is {driver}"
        )

    # remove the driver from eligible participants (until everyone has gone)
    eligible_participants.remove(driver)
    txt_eligible_participants.delete("1.0", tk.END)
    txt_eligible_participants.insert(tk.END, '\n'.join(eligible_participants))
    return


# build the application window
window = tk.Tk()
window.title("Mob Driver Picker")
window.minsize(width=250, height=250)
window.resizable(width=True, height=True)

#bind the F5 key to the choose_driver function for keyboard shortcut
window.bind('<F5>', choose_driver)

# create the widgets
txt_participants = tk.Text(master=window)
lbl_participants = tk.Label(master=window, text=PARTICIPANTS_LABEL)
txt_eligible_participants = tk.Text(master=window)
lbl_eligible_participants = tk.Label(master=window, text=ELIGIBLE_PARTICIPANTS_LABEL)
btn_choose_driver = tk.Button(master=window, text="Choose Driver", command=choose_driver)
lbl_license_info = tk.Label(master=window, text=LICENSE_MESSAGE)

# Pack the widgets
lbl_participants.pack()
txt_participants.pack()
lbl_eligible_participants.pack()
txt_eligible_participants.pack()
btn_choose_driver.pack()
lbl_license_info.pack()

# Start the mainloop
window.mainloop()
