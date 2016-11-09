#Random Function Example

import random

def fortuneTeller(numbmerToTell):
    if numbmerToTell==1:
        return 'You are good'
    elif numbmerToTell==2:
        return 'You are very good'
    elif numbmerToTell==3:
        return 'You are better'
    elif numbmerToTell==4:
        return 'You are best'
    elif numbmerToTell==5:
        return 'You are ok'
    elif numbmerToTell==6:
        return 'You are bad'


print(fortuneTeller(random.randint(1,6)))


