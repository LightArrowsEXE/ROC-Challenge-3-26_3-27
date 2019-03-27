#!/usr/bin/env python
import tkinter as tk
import webcolors as wc
import re

def toggle(button, to_send):
    if button['bg']

def colorConvert(hex):
    if re.search(r'^#(?:[0-9a-fA-F]{1,2}){3}$', hex):
        return wc.hex_to_name(hex)
    else:
        return("Invalid color code given.")

root = tk.Tk()
root.title("Additional Assignment 01")

root.resizable(False, False)

tk.Label(root, text="Fill in a hex code to change the background").pack()
convertButton = tk.Button(root, text="Convert")
convertButton.pack()

color = str(colorConvert(hex))
root.configure(background=color)

root.mainloop()

