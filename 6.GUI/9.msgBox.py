from tkinter import *
from tkinter import messagebox

def submit():
    # messagebox.showinfo(title="info message",message="you are a person")
    # messagebox.showwarning(title="info message",message="you have a virus")
    # messagebox.showerror(title="info message",message="something's wrong")
    
    # item = messagebox.askokcancel(title="title",message="do you wanna do it?")
    # if item:
    #     print("do did it!")
    # else:
    #     print("you did not do it!")
    
    item = messagebox.askretrycancel(title="title",message="do you wanna do it?")
    if item:
        print("you retry it!")
    else:
        print("you did not do it!")

window = Tk()


button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()

# 7:37:16