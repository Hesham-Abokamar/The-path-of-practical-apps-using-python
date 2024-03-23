theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def resetBoard():
    global theBoard
    theBoard = {'7': ' ', '8': ' ', '9': ' ',
                '4': ' ', '5': ' ', '6': ' ',
                '1': ' ', '2': ' ', '3': ' '}

def playAgain():
    print("Do you want to play again? (yes/no)")
    return input().lower().startswith('y')

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ". Move to which place?")

        try:
            move = input()
            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
            else:
                print("That place is already filled. Move to which place?")
                continue
        except KeyError:
            print("Invalid input please enter only from 1 to 9!")

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ' or \
               theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ' or \
               theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ' or \
               theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ' or \
               theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ' or \
               theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ' or \
               theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ' or \
               theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                if playAgain():
                    resetBoard()
                    game()
                else:
                    return
                break

        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            if playAgain():
                resetBoard()
                game()
            else:
                return

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

if __name__ == "__main__":
    game()