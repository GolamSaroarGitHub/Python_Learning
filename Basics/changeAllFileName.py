import os
print('Enter a Folder name \n')
folder=input()
cwd= os.getcwd()
print(cwd)
path=cwd+'\\'+folder
print('path: '+path)
for folderName, subfolders, filenames in os.walk(path):
    print('The current folder name is '+folderName)

    for subfolder in subfolders:
        print('The current Subfolder is '+subfolder)
    i=1
    for file in filenames:
        src=path+"\\"+str(file)
        exe=os.path.basename(file).split('.')
        exe[0]=exe[0]+str(i)
        i=i+1

        print(exe)
        file=exe[0]+'.'+exe[1]
        des=path+"\\"+str(file)
        os.rename(src,des)

print(' ')