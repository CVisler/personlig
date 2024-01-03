from tkinter import *

root = Tk()

def myClick():
    # Create label within the root widget
    label1 = Label(root, text='me clicky')
    label1.pack()


# command= executes a function
# fg = foreground color > bg = background
# hex color codes can be used -> ###### is white and 000000 is black
buttan = Button(root, text='click me', padx=50, pady=10, command=myClick, fg='red', bg='white')
buttan.pack()


# Event loop
root.mainloop()
