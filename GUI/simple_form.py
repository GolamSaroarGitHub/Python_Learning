from tkinter import *


root =Tk()


#creating the Labels and the input fields
label_1=Label(root,text='Name')

label_2=Label(root,text='Password')
entry_1=Entry(root)
entry_2=Entry(root)

#sticky has the position of North(N), East(E). . . . like that..
#for positioning it is used


label_1.grid(row=0,sticky=E)
label_2.grid(row=1,sticky=E)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)


c=Checkbutton(root,text='Keep me logged in')

## columnspan is something that will allow to get couple of column space in the grid
c.grid(columnspan=2)

root.mainloop()

