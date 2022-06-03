from tkinter import *

""" 
Creating a button and properties
"""

#Start
root = Tk()

#Function
def myClick():
    myLabel = Label(root, text="Look! I clicked a Button")
    myLabel.pack()

#Creating
myButton = Button(root, text="Click Me", command = myClick)
#   state=Disable   :    Disable button
#   padx = number , pady = number    :    Change size of button
#   fg = color, bg, color   :   Change color of button 


#Display
myButton.pack()




#Finish
root.mainloop()