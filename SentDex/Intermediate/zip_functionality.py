x=[1,2,3,4]
y=[6,7,8,9]
z=['a','b','c','d']

for a,b in zip(x,y):
    print(a,b)

for a,b,c in zip(x,y,z):
    print(a,b,c)

print(list(zip(x,y,z)))

names=['shabuz','sohel','ferdous']
grades=[96,97,98]

print(dict(zip(names,grades)))


# we can also use list comprehension

[print(a,b,c) for a,b,c in zip(x,y,z)]

import timeit

def print_to_test():
    i = 1
    for _ in range(3):
        i=i+1
    return i

print(timeit.timeit(print_to_test))


