from tkinter import *

root = Tk()

entry = Entry(root, borderwidth=5)
entry.pack()
entry.insert(0, "Enter name")

def myClick():
    # Create label within the root widget
    greeting = "Hi " + entry.get()
    label1 = Label(root, text=greeting)
    label1.pack()


# command= executes a function
# fg = foreground color > bg = background
# hex color codes can be used -> ###### is white and 000000 is black
buttan = Button(root, text='Enter your name', padx=50, pady=10, command=myClick, fg='red', bg='white')
buttan.pack()


# Event loop
root.mainloop()
