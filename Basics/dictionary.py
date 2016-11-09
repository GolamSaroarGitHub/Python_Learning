'''fruits={'name':'orange','color':'orange'}
fruits.setdefault('size','medium')
print(fruits)
##the follwoing  is not gona work as it is already set
fruits.setdefault('size','large')'''

import pprint
print('Please enterr  a setence to count the letters')
message=input()
count={}    #declaring an emmpty dictionary
for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1


pprint.pprint(count)