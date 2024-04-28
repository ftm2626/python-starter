from tkinter import *
from tkinter import colorchooser

def click():
    input = text.get("1.0",END)
    print(input)

window = Tk()
# window.geometry("420420")

text= Text(window,
           bg='light yellow',
           font=("Segoe Print",60),
           height=4,
           width=10,
           padx=20,
           pady=20,
           fg="red"
           )
text.pack()

button = Button(window, text="click", command=click)
button.pack()

window.mainloop()
