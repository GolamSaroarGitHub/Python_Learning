from tkinter import *
from tkinter import messagebox
import requests

root=Tk()

def helloCallBack(city):
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=8e96b8a4dca2cf1ed4d9d2d25842e568&units=metric")
    weather = response.json()
    cel = weather['main']['temp']
    # cel = kel * 0.0869
    messagebox.showinfo( "Weather", "%.2f"%cel+" celcius")

topFrame=Frame(root)
topFrame.pack()

secondFrame=Frame(root)
secondFrame.pack()

thirdFrame=Frame(root)
thirdFrame.pack()

bottomFrame=Frame(root)
bottomFrame.pack()

button1=Button(topFrame,text='London', fg="red",command = lambda :helloCallBack('London'))
button2=Button(topFrame,text='Dhaka', fg="green",command = lambda :helloCallBack('Dhaka'))
button3=Button(topFrame,text='New York', fg="red",command = lambda :helloCallBack('New York'))
button4=Button(topFrame,text='Sydney', fg="purple",command = lambda :helloCallBack('Sydney'))


button5=Button(secondFrame,text='Los Angeses', fg="red",command = lambda :helloCallBack('Los Angeses'))
button6=Button(secondFrame,text='Chicago', fg="green",command = lambda :helloCallBack('Chicago'))
button7=Button(secondFrame,text='Tokyo', fg="red",command = lambda :helloCallBack('Tokyo'))
button8=Button(secondFrame,text='Delhi', fg="purple",command = lambda :helloCallBack('Delhi'))

button9=Button(bottomFrame,text='Moscow', fg="red",command = lambda :helloCallBack('Moscow'))
button10=Button(bottomFrame,text='Paris', fg="green",command = lambda :helloCallBack('Paris'))
button11=Button(bottomFrame,text='Beijing', fg="red",command = lambda :helloCallBack('Beijing'))
button12=Button(bottomFrame,text='Bangkok', fg="purple",command = lambda :helloCallBack('Bangkok'))

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)


button5.pack(side=LEFT)
button6.pack(side=LEFT)
button7.pack(side=LEFT)
button8.pack(side=LEFT)


button9.pack(side=LEFT)
button10.pack(side=LEFT)
button11.pack(side=LEFT)
button12.pack(side=LEFT)

root.mainloop()