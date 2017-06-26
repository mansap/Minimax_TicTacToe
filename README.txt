Title: README for TicTacToe Game
File Name: ttt.py
Author: Mansa Pabbaraju

Input:
In the board, each move is numbered from 0 to 9.

Blank Board:        Numbered Board:
_ _ _               0 1 2
_ _ _               3 4 5
_ _ _               6 7 8

How user needs to play move:
The program asks the user to enter his/her desired move.
We need to enter a number ranging from 0 to 9 (both INCLUSIVE).
Example: If we choose 2, then the board will be updated as follows:
_ _ X             Reference: 0 1 2
_ _ _                        3 4 5
_ _ _                        6 7 8

How Computer plays it's move:
Once a user enters a move, the computer will run the Minimax algorithm and play its move.
First, the Minimax Algorithm will run, and return a move. The nodes it traverses will be displayed.
After that, Minimax Algorithm with Alpha Beta Pruning will run and return a move. The nodes it traverses will be displayed.
Both the moves generated will be equal, it is checked and displayed.
The computer then chooses this move to play and updates the board accordingly.
Now, it is again the player's chance.

Utility functions:
-1 : if computer wins
1  : if user wins
0  : if game is draw.

Result:
Move chosen by the computer, the nodes it traverses (by Minimax and Minimax with Alpha Beta Pruning both)
is shown for every board state.
The board state for every chosen move (by user and computer) is shown.
The result of the game is displayed at the end:  Draw/Won by Computer.

Observation:
The user can never win. The best possible result for the User is a Draw.
