from tkinter import *

def eventFunc(event):
    print("mouse cordinations are : ",event.x, event.y)
    return

window = Tk()


# window.bind("<Button-1>",eventFunc) # left click
# window.bind("<Button-2>",eventFunc) # middle click
# window.bind("<Button-3>",eventFunc) # right click
window.bind("<ButtonRelease>",eventFunc) 

window.mainloop()