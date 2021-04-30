board = [' ' for c in range(10)]

def insertLetter(letter,position):
    board[position] = letter

def sapceIsFree(position):
    return board[position] == ''

def printBoard(board):
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+" "+board[3])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | "+" "+board[6])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" | "+" "+board[9])
    print("   |   |   ")

def isBoardFull(board):  # sourcery skip: return-identity
    if board.count(' ') > 1:
        return False
    else:
        return True

def winner(board):
    if board[1] == board[2] == board[3]:
        print("{} wins ".format(board[1]))
    elif board[4] == board[5] == board[6]:
        print("{} wins ".format(board[4]))
    elif board[7] == board[8] == board[9]:
        print("{} wins ".format(board[7]))

    elif board[1] == board[4] == board[7]:
        print("{} wins ".format(board[1]))
    elif board[2] == board[5] == board[8]:
        print("{} wins ".format(board[1]))
    elif board[3] == board[6] == board[9]:
        print("{} wins ".format(board[1]))
    
    elif board[1] == board[5] == board[9]:
        print("{} wins ".format(board[1]))
    elif board[3] == board[5] == board[7]:
        print("{} wins ".format(board[3]))

