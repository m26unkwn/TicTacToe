#Tic Tac Toe game
board=["_", "_", "_",
       "_", "_", "_",
       "_", "_", "_"]

game_on=True

current_player= "X"


winner= None

def display_board():
     print(board[0] + " | " + board[1] + " | " + board[2])
     print(board[3] + " | " + board[4] + " | " + board[5])
     print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():

    #show intial board
    display_board()

    while game_on:


        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner=="X" or winner=="O":
        print(winner + "Won.")
    elif winner==None:
        print("Tie.")



def handle_turn(player):
    position=int(input("Enter any number in range 1-9: ")) #Here asking for user to which postion he want to put his turn
    position= position-1 # Updating the value with index value
    
    board[position]=str(input("Enter X or O: ")).upper()
    display_board()
 
def check_if_game_over():

    check_if_win()

    check_if_tie()

def check_if_win():
    
    return 


def check_if_tie():

    return

def flip_player():
    return



play_game()



