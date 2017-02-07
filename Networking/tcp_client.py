import socket


def Main():
    host='192.168.1.100'
    port=5000


    s=socket.socket()

    s.connect((host,port))

    message=input('Enter Message:')

    while message!='q':
        fmessage=message.encode()
        s.send(fmessage)
        data=s.recv(1024)

        print('Recived from server '+str(data))

        message=input('Enter Message')

    s.close()


if __name__=='__main__':
    Main()