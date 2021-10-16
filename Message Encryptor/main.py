from tkinter import *
import Encryptor

root = Tk()

msg = Entry(root)

def my_click():
    myLable = Label(root, text=e.get())
    myLable.pack()



myBtn = Button(root, text="Click!", command=my_click)
msg.pack()
myBtn.pack()


root.mainloop()