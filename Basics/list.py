players=[3,5,6]
print (players[2])
players.append(7)           # ading an item in list
print (players)
players[:2]=[0,0]
print (players)
players[:]=[]
print (players)
players.append(10)
print(players)
print(players[-1])
del players[0]
print(players)
                #### This is possible to add/remove item from list at any point
colors=["orange","blcak"]
print(colors)
colors.append('yellow')
print(colors)
colors.insert(1,'red')
print(colors)
colors.pop()
print(colors)
colors.pop(1)
print(colors)

                    ## removing a specific value

rem=[10,222,3,44,5,60,7,18,90]
rem.remove(3)
print(rem)

##             Sorting the list           ##
rem.sort()
print(rem)