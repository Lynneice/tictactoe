# --- Global Variables -----


#game board
board = ["-","-","-","-","-","-","-","-","-",]

#if game is still going
game_still_going = True

#Who won? Or tie?
winner = None

#Whose turn is it
current_player = "X"

#Display 3 x 3 tictactoe board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#Play a game of tic tac toe    
def play_game():
    
    #Display initial board
    display_board()
    #loop while game is still going
    while game_still_going:
        
        #handle a single turn of a player
        handle_turn(current_player)
        
        #Check if the game has ended
        check_if_game_over()
        
        #Flip to other player
        flip_player()
    #The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

def check_if_game_over():
    check_for_winner()
    check_if_tie()
    

def handle_turn(player):
    
    #Whose turn is it
    print(player + "'s turn.")
    position = input("Choose a position from 1-9:")
    
    valid = False
    while not valid:
        #ensures the input is within the acceptable range for board
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")
    
        position = int(position) -1
    
        if board[position] == "-":
            valid = True
        else:
            print("You cannot move there. Please select again.")
    
    board[position] = player
    
    display_board()

def check_for_winner():
    
    #Set up global variable
    global winner
    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
        #there was a win
    elif column_winner:
        winner = column_winner
        #there was a win
    elif diagonal_winner:
        winner= diagonal_winner
        #there was a win
    else:
        winner= None
    return 

def check_rows():
    global game_still_going
    #Check if rows have the same value
    row_1 = board[0]==board[1]==board[2] != "-"
    row_2 = board[3]==board[4]==board[5] != "-"
    row_3 = board[6]==board[7]==board[8] != "-"
    #if any row has a match flag a win
    if row_1 or row_2 or row_3:
        game_still_going = False
        #return winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return
    return 

def check_columns():
    global game_still_going
    #Check if columns have the same value
    column_1 = board[0]==board[3]==board[6] != "-"
    column_2 = board[1]==board[4]==board[7] != "-"
    column_3 = board[2]==board[5]==board[8] != "-"
    #if any column has a match flag a win
    if column_1 or column_2 or column_3:
        game_still_going = False
        #return winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return
  

def check_diagonals():
    global game_still_going
    #Check if diagonals have the same value
    diagonals_1 = board[0]==board[4]==board[8] != "-"
    diagonals_2 = board[6]==board[4]==board[2] != "-"
    #if any column has a match flag a win
    if diagonals_1 or diagonals_2:
        game_still_going = False
        #return winner (X or O)
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return 


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
        
    return 

def flip_player():
    #global variables
    global current_player
    #if the current player is X switch it to O
    if current_player == "X":
        current_player= "O"
    #if current player is O switch is to X
    elif current_player == "O":
        current_player = "X"
    return 
play_game()

#---Scaffolding-----
#board
#display board
#play game
#handle turn
#check win
    #check rows
    #check columns
    #check diagonals
#check tie
#flip player
