from tkinter import *

root=Tk(baseName="abcd")
root.title("hello")
def click():
    l=Label(root,text="lol").grid(column=0,row=0)
    l.pack()
b=Button(root,text="lolololol",command=click)
b.pack()

root.mainloop()