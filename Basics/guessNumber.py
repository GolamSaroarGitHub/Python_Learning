import random

guessNum=random.randint(1,20)
print('I am thinking a number between 1 to 20')
print('Try to guess the number in 6 guesses')

for guessTaken in range(1,10):
    print('please Enter your guess')
    userInput=int(input())
    if userInput < guessNum :
        print('your guess is too low')
    elif userInput>guessNum:
        print('your input is too high')
    else:
        break

if userInput==guessNum:
    print('Well done .. You have answered correct in '+str(guessTaken)+' guess')
else:
    print('Sorry... the right number i have choose was '+ str(guessNum))

