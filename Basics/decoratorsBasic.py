def outer():
    x=5
    def inner():
        print(x)
    return inner
myFunc=outer()
myFunc()

def addOne(myFunc):
    def addOneInside():
        return myFunc()+1
    return addOneInside()
@addOne
def oldFunc():
    return 3
# oldFunc=addOne(oldFunc)
print(str(oldFunc))