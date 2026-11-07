import random
board = [" "," "," "," "," "," "," "," "," ",]

def printboard():
    print("",board[0],"| ",board[1]," |",board[2],"")
    print("---+-----+---")
    print("",board[3],"| ",board[4]," |",board[5],"")
    print("---+-----+---")
    print("",board[6],"| ",board[7]," |",board[8],"")

def playerinput(board,player):
    while True:
            choice = int(input("Select the position to play your chance (1-9): "))
            if(1 <= choice <= 9 and board[choice - 1] == " "):
                board[choice - 1] = player
                break
            elif(1 <= choice <= 9 and board[choice -1] != " "):
                print("This spot is already taken!! Try Again...")
            else:
                print("Invalid move!! This spot is out of  range.")


def pick_random(board):
    comp = random.randint(0,len(board) - 1)
    if(board[comp] == " "):
        if(player == "X"):
               board[comp] = "O"
        elif(player == "O"):
               board[comp] = "X" 
    else:
        pick_random(board)

def win(board):
    if(board[0] == board[1] == board[2]):
        if(board[0] == player):
            print("You won!!")
        else:
             print("You lost!! Better Luck next time.")

    if(board[3] == board[4] == board[5]):
        if(board[3] == player):
            print("You won!!")
        else:
            print("You lost!! Better Luck next time.")
    if(board[6] == board[7] == board[8]):
        if(board[6] == player):
            print("You won!!")
        else:
             print("You lost!! Better Luck next time.")
    
    if(board[0] == board[3] == board[6]):
        if(board[0] == player):
            print("You won!!")
        else:
             print("You lost!! Better Luck next time.")

    if(board[1] == board[4] == board[7]):
        if(board[1] == player):
            print("You won!!")
        else:
             print("You lost!! Better Luck next time.")

    if(board[2] == board[5] == board[8]):
        if(board[2] == player):
            print("You won!!")
        else:
             print("You lost!! Better Luck next time.")
    if(board[0] == board[4] == board[8]):
        if(board[0] == player):
            print("You won!!")
        else:
             print("You lost!! Better Luck next time.")

    if(board[2] == board[4] == board[6]):
        if(board[2] == player):
            print("You won!!")
        else:
             print("You lost!! Better Luck next time.")

    else:
        return 0


def check_tie(board):
    flag = 0
    for el in board:
        if(el == " "):
            flag = 1
            return flag
    return flag



player = str(input("X or O: "))

printboard()
playerinput(board,player)
pick_random(board)
printboard()
playerinput(board,player)
pick_random(board)
printboard()
playerinput(board,player)
pick_random(board)
printboard()
win(board)

if(win(board) == 0):
    playerinput(board,player)
    pick_random(board)
    printboard()
else:
    print("No winner!! Replay")

