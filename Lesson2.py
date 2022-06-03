from tkinter import *

"""
Displaying labels in certain positions using grid 
"""

#Start
root = Tk()

#Create a label 
myLabel1 = Label(root, text = "Hello World!" )
myLabel2 = Label(root, text = "My name is Trevor.")

#Displaying labels 
myLabel1.grid(row=0, column = 0)
myLabel2.grid(row=1, column=1)

#Finish
root.mainloop()