board = ["1","2","3",
         "4","5","6",
         "7","8","9" ]

player1_name = "player 1"
player2_name = "player 2"
players = { }
current_player = None
winner = None
gameRunning = True

print(f"Welcome to Tic-Tac-Toe!")

#print Board
def printBoard(board):
    print( board[0] + "|" + board[1] + "|" + board[2] )
    print("------")
    print( board[3] + "|" + board[4] + "|" + board[5] )
    print("------")
    print( board[6] + "|" + board[7] + "|" + board[8] )
 #select
def setupPlayers():
    global current_player,players
    symbol=""
    while symbol not in ["X", "O"]:
      symbol = input(f"{player1_name}, choose X or O: ").upper()
    if symbol == "X":
     players["X"] = player1_name 
     players["O"] = player2_name 
    else:
     players["O"] = player1_name 
     players["X"] = player2_name   
    current_player = symbol 
    print(f" {players['X']} is X and  {players['O']} is O ")
    
#Input 
def playerinput(board):
    global current_player
    try:
     move=int(input("Enter your move (1-9): "))     
     if move>=1 and move<=9 and board[move-1] not in ["X", "O"]:
        board[move-1] = current_player
        printBoard(board) 
        return True
     else:
      print("position already taken, choose another one.")  
      return False                   
    except ValueError:
     print(f" Invalid value! please Enter your move (1-9): ")
     return False

 #check the winner
def checkRow(board):
    global winner
    for i in range(0,9,3):
        if board[i] == board[i+1] == board[i+2]:
            winner = board[i]
            return True
    return False                  
 
def checkColumn(board):
    global winner
    for i in range(3): 
        if board[i] == board[i+3] == board[i+6]:
            winner = board[i]
            return True
    return False 

def checkDiagonal(board):
       global winner
       if board[0] == board[4] == board[8]:
           winner = board[0]
           return True 
       if board[2] == board[4] == board[6]:
           winner = board[2]
           return True
       return False
   
#check tie   
def checkTie(board):
    global gameRunning
    if all(pos in ["X", "O"] for pos in board):
        printBoard(board)
        print("It's a tie!")
        gameRunning = False
                              
                              
def checkWin():
    if checkDiagonal(board) or checkColumn(board) or checkRow(board):
        printBoard(board)
        print(f"The winner is {players[winner]} ({winner})!")
        print(f"Thanks for playing Tic-Tac-Toe!")
        gameRunning = False
        return True
    return False         

def switchplayer(board):
    global current_player
    if current_player =="X":
        current_player ="O"
    else:
        current_player ="X"
    print(f" turn of {players[current_player]} ({current_player})")    
          
if __name__== "__main__":  
 printBoard(board)
 setupPlayers( )            
while gameRunning:

    if playerinput(board):
     if checkWin():
       break
     checkTie(board)  
     if not gameRunning:
        break
     switchplayer(board)
    