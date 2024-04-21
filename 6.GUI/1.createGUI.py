from tkinter import *

# widgets = GUI elements : buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() #instantiate an instace of window

window.geometry("420x420")

window.title("Hello python")

window.config(background="pink")

# icon = PhotoImage(file="logo.png") 
# window.iconphoto(True,icon)

window.mainloop() #shows window

