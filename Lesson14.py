from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()

#   Databases

#   Create a database or connect one 
conn = sqlite3.connect('address_book.db')

#   Create cursor 
c = conn.cursor()

#   Create table 
c.execute("""CREATE TABLE adresses (
    first_name text, 
    last_name text, 
    address text, 
    city text, 
    state text, 
    zipcode integer
    )""")


#   Commit changes
conn.commit()


#Close connections 
conn.close()

root.mainloop()