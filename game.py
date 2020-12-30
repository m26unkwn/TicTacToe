#Tic Tac Toe game
board=["_", "_", "_",
       "_", "_", "_",
       "_", "_", "_"]

def display_board():
     print(board[0] + " | " + board[1] + " | " + board[2])
     print(board[3] + " | " + board[4] + " | " + board[5])
     print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():

    #show intial board
    display_board()

    handle_turn()


def handle_turn():
    position=input("Enter any number in range 1-9:")
    

play_game()