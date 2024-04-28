from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    window.config(bg=colorHex)

window = Tk()
# window.geometry("420420")

button = Button(window, text="click", command=click)
button.pack()

window.mainloop()
