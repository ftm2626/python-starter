from tkinter import *
from tkinter import ttk

window = Tk()


notebook = ttk.Notebook(window) #widget that manages a collection of windows and displays

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1,text="tab 1")
notebook.add(tab2,text="tab 2")
notebook.pack()

Label(tab1,text="tab number1").pack()
Label(tab2,text="tab number2").pack()


window.mainloop()