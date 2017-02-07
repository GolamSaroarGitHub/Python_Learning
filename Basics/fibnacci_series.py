
class Fib:
    def Main(self):
        x=int(input('Enter the number of fibonacci you wish to generate\n'))

        a,b=0,1
        for number in range(x):

            a,b=b,a+b
            print(str(b), end=' ')

fib_num=Fib()
fib_num.Main()