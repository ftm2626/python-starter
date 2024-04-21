from tkinter import *

def click():
    print("clicked")

window = Tk()

button = Button(window,
                text="hello button",
                command=click)
button.pack()

window.mainloop()


# 6:31:03