from tkinter import *

root=Tk()

root.wm_title("Shabuz")
canvas=Canvas(root,width=200,height=100)
canvas.pack()
greenBox=canvas.create_rectangle(25,25,130,60,fill="green")

root.mainloop()