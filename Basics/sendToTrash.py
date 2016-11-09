import send2trash

newFile=open('newFile.txt','w')
newFile.write('This is a good example')
newFile.close()
send2trash.send2trash('newFile.txt')