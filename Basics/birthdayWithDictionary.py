
birthday={'ferdous':'Dec 1','sohel':'July 18'}
for i in birthday.items():
    print(i)
for k in birthday.keys():
    print(k)


for v in birthday.values():
    print(v)

while True:
    print('please enter the name to find their Birthday')
    name=input()
    if name in birthday:
        print(birthday[name]+' is the birthday for '+name)
    elif name=='':
        break
    else:
        print('I do not have their birthday information.\n Please enter their birthday')
        bday=input()
        birthday[name]=bday
        print('The birthday database Updated')

print(birthday)