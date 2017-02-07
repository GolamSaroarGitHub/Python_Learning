import socket
import time
#
# host='127.0.0.1'
# port=5002
#
# clients=[]
#
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# s.bind((host,port))
# s.setblocking(0)
#
# quiting=False
# print('server started')
#
# while not quiting:
#     try:
#         data,addr=s.recvfrom(1024)
#         if "Quit" in str(data):
#             quiting=True
#         if addr not in clients:
#             clients.append(addr)
#
#         print(time.ctime(time.time)+str(addr)+' : '+str(data))
#
#         for clint in clients:
#             byte_message = data.encode()
#             s.sendto(byte_message,clint)
#     except:
#         pass
# s.close()


host = '127.0.0.1'
port = 5005

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

quitting = False
print('Server Started')
while not quitting:
    try:
        data, addr = s.recvfrom(1024)
        if "Quit" in str(data):
            quitting = True
        if addr not in clients:
            clients.append(addr)

        print(time.ctime(time.time()) + str(addr) + ": :" + str(data))
        for client in clients:
            byte_message = data.decode('utf-8')
            s.sendto(byte_message,client)
            # s.sendto(data, client)
    except:
        pass
s.close()