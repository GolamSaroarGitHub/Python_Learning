import os

for folderName, subfolders, filenames in os.walk(r'G:\Python'):
    print('The current folder name is '+folderName)

    for subfolder in subfolders:
        print('The current Subfolder is '+subfolder)

    for file in filenames:
        print('The current file name is '+file)

print(' ')