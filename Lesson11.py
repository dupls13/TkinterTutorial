from tkinter import *
from PIL import ImageTk, Image


root = Tk()

def open():
    top = Toplevel()
    lbl = Label(top, text = "Hello world").pack()   
    rks = Label(root, text = "Whats up").pack()
    
    btwn2 = Button(top, text= "Close Window", command=top.destroy).pack()

    


butn = Button(root, text = "Open second window", command = open).pack()


mainloop()