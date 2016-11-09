import random

board=[0,1,2,
       3,4,5,
       6,7,8]
def show():
    print(str(board[0])+'   |   '+str(board[1])+'   |   '+str(board[2]))
    print('-------------------')
    print(str(board[3])+'   |   '+str(board[4])+'   |   '+str(board[5]))
    print('-------------------')
    print(str(board[6])+'   |   '+str(board[7])+'   |   '+str(board[8]))

show()

def chekLine(char,spot1,spot2,spot3):
    if board[spot1]==char and board[spot2]==char and board[spot3]==char:
        return True
def checkAll(char):
    if chekLine(char,0,1,2):
        return True
    if chekLine(char,0,3,6):
        return True
    if chekLine(char,1,4,7):
        return True
    if chekLine(char,2,5,8):
        return True
    if chekLine(char,3,4,5):
        return True
    if chekLine(char,6,7,8):
        return True
    if chekLine(char,0,4,8):
        return True
    if chekLine(char,2,4,6):
        return True

while True:
    userInput=int(input('Select Your spot\n'))
    if board[userInput]!='X' and board[userInput] !='0':
        board[userInput]='X'
        show()
        if checkAll('X')==True:
            print('You win')
            break
        while True:
         random.seed()
         opponent=random.randint(0,8)
         # opponent =int(input('Select Opponents spot\n'))
         if board[opponent] != 'X' and board[opponent] != '0':
            board[opponent] = 'O'
            show()
            if checkAll('O') == True:
                print('Opponent wins')
                break
            break

    else:
        print('This spot is taken')
    show()