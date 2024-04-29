# frame: a rectacular container to group and hold widgets 
from tkinter import *

def create_window():
    # new_window  = Toplevel() #a new window on top of the other windows, linked to a bottom window
    new_window  = Tk() #new independent window
    
    old_window.destroy()


old_window = Tk()

Button(old_window, text="create new window",font=("Consolas",25),width=3,command=create_window).pack()

old_window.mainloop()

