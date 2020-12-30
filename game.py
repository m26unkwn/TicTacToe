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
    #main part of the game where game is going
    while game_on:

        #to handle which player is playing

        handle_turn(current_player)

        #check whether there game is over or not
        check_if_game_over()

        #For flipping the player
        flip_player()

    if winner=="X" or winner=="O":
        print(winner + " Won.")
    elif winner==None:
        print(" Tie.")



def handle_turn(player):


    print(player+"'s, turn")

    #Here asking for user to which postion he want to put his turn
    position=input("Enter any number in range 1-9: ")
    valid=False
    while not valid:
        while position not in["1", "2", "3", "4", "5", "6" , "7", "8", "9"]:
            position=input("Invalid input choose a position in range 1-9: ")
            
        position= int(position)-1 # Updating the value with index value

        if board[position]=="_":
            valid=True
        else:
            print("Position is filled. Try Again!")
        
        board[position]=player

    
    display_board()
 
def check_if_game_over():

    check_for_winner()

    check_if_tie()

def check_for_winner():
    global winner
    #checkforRow
    row_winner=check_row()
    #checkForcol
    col_winner=check_col()
    #check For Coldiagnol winner
    diagnol_winner=check_diagnol()

    if row_winner:
        winner=row_winner
    
    elif col_winner:
        winner=col_winner

    elif diagnol_winner:
        winner=diagnol_winner

    else:
        winner=None

    return 



def check_if_tie():
    global game_on
    if "_" not in board:
        game_on=False

    return




def check_row():
    global game_on
    row_1=board[0]==board[1]==board[2] != "_"
    row_2=board[3]==board[4]==board[5] != "_"
    row_3=board[6]==board[7]==board[8] != "_"
    
    if row_1 or row_2 or row_3:
        game_on= False

    if row_1:
        return board[0]

    elif row_2:
        return board[3]

    elif row_3:
        return board[6]    

    return


def check_col():
    global game_on
    col_1=board[0]==board[3]==board[6] != "_"
    col_2=board[1]==board[4]==board[7] != "_"
    col_3=board[2]==board[5]==board[8] != "_"
    
    if col_1 or col_2 or col_3:
        game_on= False

    if col_1:
        return board[0]

    elif col_2:
        return board[1]

    elif col_3:
        return board[2]    

    return


def check_diagnol():
    global game_on
    diagnol_1=board[0]==board[4]==board[8] !="_"
    diagnol_2=board[2]==board[4]==board[6] !="_"

    if diagnol_1 or diagnol_2:
        game_on=False
    if diagnol_1:
        return board[0]
    elif diagnol_2:
        return board[2]

    return
    

def flip_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"
    return


play_game()



