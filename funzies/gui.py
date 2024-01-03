from tkinter import *

root = Tk()

""" Create the things """
label1 = Label(root, text='hej')
label2 = Label(root, text='hejsa')

""" Put the things on the screen """
label1.grid(row=0, column=1)
label2.grid(row=1, column=0)

# Event loop
root.mainloop()
