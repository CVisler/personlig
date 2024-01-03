""" ENTRY BOX """

from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

root = tb.Window(themename='superhero')
root.title('SMSP Dashboard')
# root.iconbitmap('img/sony.jpg')
root.geometry('500x350')

# Create entry function
def speak():
    label1.config(text=f'You typed: {entry.get()}')

# Create entry (can also do show="*")
entry = tb.Entry(root, foreground='red')
entry.pack(pady=50)

# Create a button
button1 = tb.Button(root, bootstyle="danger outline", text="Do the click", command=speak)
button1.pack(pady=20)

# Create label
label1 = tb.Label(root, text="")
label1.pack(pady=20)







root.mainloop()
