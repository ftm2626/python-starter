from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(title="open file to read",
                                          filetypes=(("text files",".txt"),("all files","*.*"))
        
    )
    file = open(filepath,"r")
    print(file.read())
    file.close() 
    
    
def saveFile():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("Text file",".html"),
                                        ("Text files",".*"),
                                    ])
    fileText= str(text.get(1.0,END))
    file.write(fileText)
    file.close()
    
    if file is None:
        return

window = Tk()
# window.geometry("420420")


text = Text(window)
text.pack()

button = Button(window, text="open", command=openFile)
button.pack()

buttonSave = Button(window, text="save", command=saveFile)
buttonSave.pack()

window.mainloop()


# 08:05:15