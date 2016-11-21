import threading
import time
class Messanger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.Thread.getName(self))

x=Messanger(name='Sending Message')
y=Messanger(name='Recieving Message')

x.start()
y.start()