# first we need an example list:
x = [1,6,3,2,6,1,2,6,7]
# lets add something.
# we can do .append, which will add something to the end of the list, like:
x.append(55)
print(x)

x.insert(2,33)
print(x)

x.remove(6)
print(x)

print(x.index(2))

x.sort()
print(x)

y = ['Jan','Dan','Bob','Alice','Jon','Jack']
y.sort()
print(y)
y.reverse()
print(y)

x = [[2,6],[6,2],[8,2],[5,12]]
print(x[2])