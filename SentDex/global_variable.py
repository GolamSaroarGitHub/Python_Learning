x = 6
y=6
def example2():
    # works
    print(x)
    print(x+5)

    # but then what happens when we go to modify:
    # x+=6

    # so there we attempted to take the x var and add 6 to it... but now
    # we are told that we cannot, as we're referencing the variable before
    # its assignment.
    global y
    y+=5
    print('y ',y)
example2()
print(y)