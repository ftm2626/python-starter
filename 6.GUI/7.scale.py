from tkinter import *

def submit():
    print("the temp is " , scale.get(), "degrees")

window = Tk()

scale = Scale(window, 
              from_=0,
              to=100,
              length=600,
              orient=VERTICAL,
              tickinterval=25
              )
scale.set(50)
scale.pack()


button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()

