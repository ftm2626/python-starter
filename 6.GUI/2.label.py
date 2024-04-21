# label : an area widget that holds text and/or an image within a window

from tkinter import *


window = Tk()

label = Label(window,
              text="hello label",
              font=("Arial",50,"bold"),
              fg="green",
              bg="red",
              relief=RAISED,
              bd=10,
              padx=10)
              #   image="photo.jpg"

              
# label.pack() #same as .place
label.place(x=0,y=0)

window.mainloop()