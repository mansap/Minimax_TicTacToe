# FileName : ttt.py
#
# Implementation of Tic Tac Toe game using:
#          1. Minimax Algorithm
#          2. Minimax Algorithm with Alpha Beta Pruning
#
# Description: Tic Tac Toe is played between Human and Computer.
#              Human: 'X' icon and Computer: 'O' icon.
#              Human player starts playing first.
#
# Author: Mansa Pabbaraju

flag = True
gameWinFlag = False
gameDrawFlag = False
board =[y for y in range(9)]
used = [ y for y in range(9)]
# empty list for all the good possible moves
goodMoves = []
drawMoves = []
valid = [0,1,2,3,4,5,6,7,8]


def boardInit():
    for row in range (0,9):
        board[row] = '_'
        used[row] = False

def ShowCurrBoard():
    print ('  ' + board[0] + '  ' + board[1] + '  ' + board[2] + '  ')
    print ('  ' + board[3] + '  ' + board[4] + '  ' + board[5] + '  ')
    print ('  ' + board[6] + '  ' + board[7] + '  ' + board[8] + '  ')


#####################################################################
#              Minimax with Alpha-Beta Pruning                      #
#####################################################################

# takes the move from the player, computer prepares for next move
# using Minimax Algorithm (uses DFS to save on memory)
def processMoveAlphaBeta():

    global used,goodMoves,board,drawMoves,lossMoves,count
    count = 0
    # after search tree, computer returns its best move
    value = -3
    alpha = -1 # best alternative for MAX (player X) along path to state
    beta = 1 # best alternative for MIN (player O) along path to state
    for move in valid:
        if used[move] == False:
            count += 1
            board[move] = 'O'
            used[move] = True
            value = Max_ValAB(board,used,alpha,beta)
            board[move] = '_'
            used[move] = False
            #win
            if value == -1:
                goodMoves = [move]
            #draw
            if value == 0:
                drawMoves.append(move)

    if len(goodMoves) > 0:
        temp = goodMoves[0]
    else:
        temp = drawMoves[0]
    goodMoves = []
    drawMoves = []
    return temp

def Max_ValAB(board,used,alpha,beta):
    global valid,count
    if checkWin():
        if Winner == 'X':
            return 1
        else:
            return -1

    if checkDraw():
        return 0

    v = -10
    for move in valid:
        if used[move] == False:
            count+=1
            board[move] = 'X'
            used[move] = True
            v = max(v,Min_ValAB(board,used,alpha,beta))
            board[move] = '_'
            used[move] = False
            if v >= beta:
                return v
            alpha = max(alpha,v)
    return v

def Min_ValAB(board,used,alpha,beta):
    global valid,count
    if checkWin():
        if Winner == 'X':
            return 1
        else:
            return -1

    if checkDraw():
        return 0

    v = +10
    for move in valid:
        if used[move] == False:
            count += 1
            board[move] = 'O'
            used[move] = True
            v = min(v,Max_ValAB(board,used,alpha,beta))
            board[move] = '_'
            used[move] = False
            if v <= alpha:
                return v
            beta = min(beta,v)
    return v



#####################################################################
#              Minimax without Alpha-Beta Pruning                   #
#####################################################################


# takes the move from the player, computer prepares for next move
# using Minimax Algorithm (uses DFS to save on memory)
def processMove():

    global used,goodMoves,board,drawMoves,lossMoves,count
    count = 0
    # after search tree, computer returns its best move
    value = -3
    for move in valid:
        if used[move] == False:
            count+=1
            board[move] = 'O'
            used[move] = True
            value = Max_Val(board,used)
            board[move] = '_'
            used[move] = False
            #win
            if value == -1:
                goodMoves = [move]
            #draw
            if value == 0:
                drawMoves.append(move)

    if len(goodMoves) > 0:
        temp = goodMoves[0]
    else:
        temp = drawMoves[0]
    goodMoves = []
    drawMoves = []
    return temp

def Max_Val(board,used):
    global valid,count
    if checkWin():
        if Winner == 'X':
            return 1
        else:
            return -1

    if checkDraw():
        return 0

    v = -10
    for move in valid:
        if used[move] == False:
            count+=1
            board[move] = 'X'
            used[move] = True
            v = max(v,Min_Val(board,used))
            board[move] = '_'
            used[move] = False
    return v

def Min_Val(board,used):
    global valid,count
    if checkWin():
        if Winner == 'X':
            return 1
        else:
            return -1

    if checkDraw():
        return 0

    v = +10
    for move in valid:
        if used[move] == False:
            count+=1
            board[move] = 'O'
            used[move] = True
            v = min(v,Max_Val(board,used))
            board[move] = '_'
            used[move] = False
    return v


def max(a,b):
    if a>b:
        return a
    return b

def min(a,b):
    if a<b:
        return a
    return b

def setMoveOnBoard(move, icon):
    global used
    used[move] = True
    board[move] = icon
    ShowCurrBoard()

def StartPlay():
    global r,NewCcol,gameWinFlag,gameDrawFlag,flag,Winner,currMove,bestMove,valid,used,bestMove1
    while not (checkWin() or checkDraw()):
        # player's move
        if flag:
            print()
            currMove = int(input ('Enter next move:'))
            # error check
            while used[currMove] == True:
                print('Incorrect move, try again')
                currMove = int(input ('Enter next move:'))
            print()
            print('After your move, board is: ')
            setMoveOnBoard(currMove, 'X')
            valid.remove(currMove)
            flag = False
        else:
            print('Simple Minimax Algorithm')
            bestMove1 = processMove()
            print()
            print('With Simple Minimax, Computer chooses Move: ', bestMove1)
            print('Simple Minimax, Nodes traversed : ', count)
            print()
            print('Minimax Algorithm with Alpha-Beta Pruning')
            print()
            bestMove = processMoveAlphaBeta()
            if bestMove == bestMove1:
                print('Both the algorithms return the same move')
            print()
            print('With Minimax Alpha-Beta pruning, Computer chooses Move: ', bestMove)
            print('Minimax with Alpha-Beta Pruning, Nodes traversed : ', count)
            print()
            print('After Computer move, board is: ')
            setMoveOnBoard(bestMove, 'O') # computer plays it's move
            valid.remove(bestMove)
            flag = True # computer's turn over, now player's turn

    if checkWin():
        if Winner == 'X':
            win = 'player'
        else:
            win = 'computer'
        print()
        print('Game over, Won by '+ win + ' with icon '+ Winner)

    elif gameDrawFlag:
        print('Game is a Draw')

# check for draw in game
def checkDraw():
    global gameDrawFlag
    for row in range(0,9):
        if used[row] == False:
            gameDrawFlag = False
            return False
    gameDrawFlag = True
    return True

def checkWin():
    lst = ['X','O']
    global Winner,gameWinFlag
    for icon in lst:

        # to keep track of winner
        Winner = icon
        # check row win
        if (board[0] == board[1] == board[2] == icon) | \
                (board[3] == board[4] == board[5] == icon) | \
                (board[6] == board[7] == board[8] == icon):
           gameWinFlag = True
           return True

        # check col win
        if (board[0] == board[3] == board[6] == icon) | \
                (board[1] == board[4] == board[7] == icon) | \
                (board[2] == board[5] == board[8] == icon):
           gameWinFlag = True
           return True

        # check diagonal wins
        if (board[0] == board[4] == board[8] == icon) | \
                (board[2] == board[4] == board[6] == icon):
           gameWinFlag = True
           return True

    return False

def main():
    global board
    boardInit()
    print()
    ShowCurrBoard()
    print()
    print('Game begins!')
    print('Play your move, your symbol is X')
    StartPlay()

main()