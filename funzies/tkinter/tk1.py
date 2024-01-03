""" INTRO """

from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

counter = 0
def button_thing():
    global counter
    counter += 1
    label_count.config(text=counter)
    if counter % 2 == 0:
        label_head.config(text='Welcome')
    else:
        label_head.config(text='Not welcome')


root = tb.Window(themename='sandstone')
root.title('SMSP Dashboard')
# root.iconbitmap('img/sony.jpg')
root.geometry('500x350')


label_head = tb.Label(text='Welcome', font=('Helvetica', 20))
label_head.pack(pady=50)

label_count = tb.Label(text=counter)
label_count.pack(padx=25, pady=25)


button = tb.Button(text='Submit', bootstyle="danger, outline", command=button_thing)
button.pack(pady=15)

root.mainloop()
