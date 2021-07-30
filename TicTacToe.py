#Author: Emil
#Description: Two player tictactoe game

import time

#create a dictionary to hold our board's slot number and space to enter X or O
board = {'1': ' ' , '2': ' ' , '3': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '7': ' ' , '8': ' ' , '9': ' ' }
p1name = ''
p2name = ''

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

#function that'll introduce program and will only run when program is first started
def start():
    global p1name
    global p2name
    print("Welcome to our two player Tic Tac Toe!\n")
    p1name = input("What's player one's name?: ")
    p2name = input("What's player two's name?: ")

    print("\nHey",p1name,"and",p2name,"! Let's get started")

    print("Enter which the slot number you want to enter your X or O based off of this: ")
    print(""" 
            1|2|3
            -+-+-
            4|5|6
            -+-+-
            7|8|9""")
    print("\n========Game Start========")

# our main function which let us play our game
def game():
    global p1name
    global p2name
    name = p1name #the name of whoever's turn it is. Player 1 starts
    current = 'X'
    turn = 0

    for i in range(10): #range is 10 because after that, the board would be filled
        printBoard(board)
        time.sleep(1)
        if current == 'X':
            move = input(name + " it's your turn. Where do you place your X?: ")
            
        else:
            move = input(name + " it's your turn. Where do you place your O?: ")
            
        while True:
            if board[move] == ' ': #if the spot isn't occupied, we'll enter the X or O
                board[move] = current
                turn += 1
                break
            else:
                move = input("That place is already filled.\nMove to which place?: ") 

        #after 5 turns, we'll keep checking if any player won or not
        if turn>=5:
            if board['7'] == board['8'] == board['9'] != ' ': # across the top
                printBoard(board)
                print("========Game Over========\n",name, " wins!")
                
                break
            elif board['4'] == board['5'] == board['6'] != ' ': # across the middle
                printBoard(board)
                print("========Game Over========\n",name, " wins!")

                break
            elif board['1'] == board['2'] == board['3'] != ' ': # across the bottom
                printBoard(board)
                print("========Game Over========\n",name, " wins!")

                break
            elif board['1'] == board['4'] == board['7'] != ' ': # down the left side
                printBoard(board)
                print("========Game Over========\n",name, " wins!")

                break
            elif board['2'] == board['5'] == board['8'] != ' ': # down the middle
                printBoard(board)
                print("========Game Over========\n",name, " wins!")

                break
            elif board['3'] == board['6'] == board['9'] != ' ': # down the right side
                printBoard(board)
                print("========Game Over========\n",name, " wins!")

                break 
            elif board['7'] == board['5'] == board['3'] != ' ': # diagonal
                printBoard(board)
                print("========Game Over========\n",name, " wins!")

                break
            elif board['1'] == board['5'] == board['9'] != ' ': # diagonal
                printBoard(board)
                print("========Game Over========\n",name, " wins!")

                break 

        if turn == 9:
            print("========Game Over========\n")
            time.sleep(1)
            print("It's a Tie!")
            break

        if current == 'X':
            current = 'O'
            name = p2name
        else: 
            current = 'X'
            name = p1name

    #ask the players if they want to play again or not
    restart = input("Do want to play again?(Y/N)").lower()
    if restart == "y":  
         for key in board:
             board[key] = ' '
         time.sleep(1)
         game()
    else: 
        time.sleep(1)
        print("Hope you had fun, see you later!")

if __name__ == "__main__":
    start()
    game()
