
'''
The enumerate function returns a tuple containing the count,

and then the actual value from the iterable.
'''
example=['left','right','up','down']

for i,j in enumerate(example):
    print(i,j)

#That iterable can be a dict:
example_dict = {'left':'<','right':'>','up':'^','down':'v',}
for i,j in enumerate(example_dict):
    print(i,j)

# [print(i,j) for i,j in enumerate(example_dict)]