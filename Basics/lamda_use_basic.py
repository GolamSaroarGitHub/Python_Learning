

def printX(a):
    return lambda x: x+a

f=printX(5)

print(f(8))
print(printX(8)(7))