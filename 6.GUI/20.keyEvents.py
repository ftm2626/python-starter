from tkinter import *

def eventFunc(event):
    print("you pressed : ",event.keysym)
    return

window = Tk()

# window.bind("<w>",eventFunc)
window.bind("<Key>",eventFunc)

window.mainloop()