# def squar_numbers(nums):
#     result=[]
#     for i in nums:
#         result.append(i*i)
#     return result
# my_nums=squar_numbers([2,3,4,5,6])
# print(my_nums)

#####Output:  [4, 9, 16, 25, 36]




def squar_numbers(nums):
    for i in nums:
        yield (i*i)
my_nums=squar_numbers([2,3,4,5,6])
for num in my_nums:
    print(num)

"""
 OutPut
4
9
16
25
36
"""