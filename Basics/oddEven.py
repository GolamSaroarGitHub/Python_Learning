numbers=[1,8,5,42,25,26,3,10]
x=''
print('The numbers are ')
for n in numbers:
    x=x+' '+str(n)
print(x)
odd=[]
even=[]
while len(numbers)>0:
    num=numbers.pop()
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)

print('The even numbers are',end=" ")
print(even)
print('The odd numbers are',end=" ")
print(odd)
