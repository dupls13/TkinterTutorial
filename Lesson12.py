from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog 

root = Tk()

root.filename = filedialog.askopenfilename(initialdir='/Users/trevor/Documents', title="Select a file", filetypes = (("all files", "*.*")))

root.mainloop()