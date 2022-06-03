from tkinter import *

"""
Input tutorial wth button and display 
"""


#Start
root = Tk()

#Entry Widget 
entry = Entry(root, borderwidth=5)
"""   width = value   :   Change size 
   bg, fg  :   Change color
"""

#entry.insert(0, "Enter your Name: ")

#Function
def myClick():
    hello = "Hello " + entry.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

#Button Display
myButton = Button(root, text="Enter your name", command = myClick)




#Display
entry.pack()
myButton.pack()





#Finish
root.mainloop()