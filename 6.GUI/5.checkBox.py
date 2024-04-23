from tkinter import *


def submit():
    if(x.get()==1):
        print("you agree")
    else:
        print("you disagree! :)")

window = Tk()
x = IntVar() 

chack_button = Checkbutton(window,
                           text="i agree to sth",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=submit)


chack_button.pack()

window.mainloop()

