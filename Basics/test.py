
import subprocess as sp
import os


def print_menu():
    # sp.call('cls', shell=True)

    print('#### Enter a number greater than 2  ')
    print('1. Refresh')
    print('0. Exit')

# def clear():
clear= lambda: os.system('cls')

print_menu()
while True:

    x = int(input('Enter a number: \n').strip())

    if (x % 2 != 0 and x>1):
        print('Weird')
    elif ((x % 2 == 0) and x in range(2, 6)):
        print('Not weired')
    elif ((x % 2 == 0) and x in range(6, 21)):
        print('Weired')
    elif ((x % 2 == 0) and x > 20):
        print('Weired')
    elif x == 1:
        clear()
        print_menu()

    elif x == 0:
        break





