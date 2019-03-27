import tkinter as tk
from PIL import Image, ImageTK

cars = [
    "Audi",
    "Ferrarri",
    "Ford",
    "Mercedes",
    "Opel"
]

def grab_img(event):
    pass

root = tk.Tk()
root.title("Additional Assignment 02")

root.set(cars[0])

tk.Label("Select a car to showcase it").pack()
form = root.optionmenu()

root.mainloop()