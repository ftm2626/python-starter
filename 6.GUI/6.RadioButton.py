from tkinter import *

food = ["pizza","burger","hotdog"]

window = Tk()

x= IntVar()

for i in range(len(food)):
    radio_button = Radiobutton(window, text=food[i],variable=x, value=i)
    radio_button.pack(anchor=W)


window.mainloop()

# 7:00:45