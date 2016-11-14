import random

heads=0
tails=0

for i in range(0,100):
    num=random.randint(0,1)
    if num==0:
        heads+=1
    else:
        tails+=1
print('Heads count %i' %heads)
print('Tails count %i' %tails)
