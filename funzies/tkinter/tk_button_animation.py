import tkinter as tk

root = tk.Tk()
root.geometry('300x500')
root.configure(bg='#141414')


def button(x, y, text, bcolor, fcolor):
    def on_enter(e):
        myButton['background'] = bcolor
        myButton['foreground'] = fcolor

    def on_leave(e):
        myButton['background'] = fcolor
        myButton['foreground'] = bcolor

    myButton = tk.Button(
            root,
            width=30,
            height=5,
            text=text,
            fg=fcolor,
            bg=bcolor,
            border=0,
            activeforeground=fcolor,
            activebackground=bcolor,
            command=None,)

    myButton.bind("<Enter>", on_enter)
    myButton.bind("<Leave>", on_leave)

    myButton.pack()


button(0,0,'test','#ffcc66','#141414')
root.mainloop()
