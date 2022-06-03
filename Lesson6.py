from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to Code at Codemy.com")
#root.iconbitmap('/Users/trevor/Documents/Python/Defender/player.png')

my_img = ImageTk.PhotoImage(Image.open('/Users/trevor/Documents/Python/Defender/player.png'))
my_label = Label(image=my_img)
my_label.pack()






button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()






root.mainloop()