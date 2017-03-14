names = ['Jeff', 'Gary', 'Jill', 'Samantha']
for name in names:
    print(','.join(name))
   # print('Hello there '.join(name))

for name in names:
    statement = ' '.join(['Hello there', name]) ## Here ' ' is a conncector that will connect both the "hello there" and name variable
    print(statement)

'''
We have used fill in the gaps . we can do the similar activities with the
variable declared and used it in format later
'''

who = 'Golam Saroar'
how_many = 12

print('{} bought {} apples today!'.format(who, how_many))

xyz = (i for i in range(50))
print(list(xyz)[-5:])