""" COMBO BOX """

from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

root = tb.Window(themename='sandstone')
root.title('SMSP Dashboard')
# root.iconbitmap('img/sony.jpg')
root.geometry('500x350')

def button_click():
    label_head.config(text=f'{combo.get()} clicked.')


# Need to pass an event to the function
def second_click(event):
    label_head.config(text=f'{combo.get()} clicked.')


style1 = tb.Style()
style1.configure('success.Outline.TButton', font=('Helvetica', 18))

label_head = tb.Label(text='Welcome', font=('Helvetica', 18))
label_head.pack(pady=30)

# Create dropdown list for combo box
days = ['Monday', 'Tuesday', 'Wednesday']

# Create combobox
combo = tb.Combobox(root, bootstyle='success', values=days)
combo.pack(pady=20)

# Set combo default
combo.current(0)

button = tb.Button(root, text='Submit', style='success.Outline.TButton', width=15, command=button_click)
button.pack(pady=20)

# Bind combobox
combo.bind("<<ComboboxSelected>>", second_click)

root.mainloop()
