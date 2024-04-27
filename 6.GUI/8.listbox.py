from tkinter import *

def submit():
    item = listbox.get(listbox.curselection())
    print(item)

window = Tk()

listbox = Listbox(window,
                  font=("Constantia",35),
                  width=12)
listbox.pack()
listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"burger")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())


button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()

