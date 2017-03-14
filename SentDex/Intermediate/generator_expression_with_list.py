input_list=[1,2,5,8,9,7,10]

def div_by_five(i):
    if i%5==0:
        return True
    else:
        return False

xyz=(i for i in input_list if div_by_five(i))

print(list(xyz))  #