from tkinter import *

root=Tk()

one=Label(text="One",bg="red",fg="white")
two=Label(text="Two",bg="green",fg="black")
three=Label(text="Three",bg="blue",fg="white")

one.pack()
two.pack(fill=X)
three.pack(side=RIGHT,fill=Y)

root.mainloop()
