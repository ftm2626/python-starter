from tkinter import *

# entry widget : textbox that accepts a single line of user input
def submit():
    username = entry.get() # get input value
    print(username)
    entry.delete(0,END) # delete value of input
    entry.config(state=DISABLED)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
              font=("Arial",20),
              show="*" #FOR PASSWORD    
              )

entry.insert(0,"enter name here")
entry.pack()

submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

back_button = Button(window, text="backspace", command=backspace)
back_button.pack(side=RIGHT)

window.mainloop()