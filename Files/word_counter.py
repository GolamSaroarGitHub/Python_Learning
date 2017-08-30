

with open("search_file.txt",'r') as f:
    data=f.read()
    f.close()
    words=data.split(' ')

print("Total Words in the file are: "+str(len(words)))
