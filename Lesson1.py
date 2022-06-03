from tkinter import *

"""
Introduction to tkinter. 
Making a label and packing it into display.
"""

#Start 
root = Tk()


#Creating Label
myLabel = Label(root, text = "Hello world!")

#Place label 
myLabel.pack()


#Finish
root.mainloop()

