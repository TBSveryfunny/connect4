def check4Winner(col, token):
    # This method checks for the winner of the game. 
    # This is accomplished by scanning for every possible 
    # win condition for each way to win: 
    # vertical, horizontal, ascending diagonal, and descending diagonal.

    # Vertical wins
    for i in range(0, 7):
      for index in range(0, 3):
        if col[i][index:index + 4].count("| " + token + " ") == 4:
          return True

    # Horizontal wins
    possib = []
    for i in range(0, 4):
      for index in range(0, 6):
        if [col[i+j][index] for j in range(0, 4)].count("| " + token + " ") == 4:
          return True

    # Diagonal wins (ascending)
    for i in range(0, 4):
      for index in range(0, 3):
        if [col[i+j][index+j] for j in range(0, 4)].count("| " + token + " ") == 4:
          return True

    # Diagonal wins (descending)
    for i in range(0, 4):
      for index in range(0, 3):
        if [col[i+(3-j)][index+j] for j in range(0, 4)].count("| " + token + " ") == 4:
          return True
    
    return False

def renderBoard(col):
    # This method displays the board.
    # Had to reverse the For loop so gravity worked properly.
    for index in range(5, - 1, -1):
      for index2 in range(0, 7):
        print(col[index2][index], end="")
      print("|")
    print("The current state of the board.")

def displayPrompt(player, pindex, token):
    # displays the prompt for the user to drop their token.
    print(player[pindex] + " (player " + token + "), please enter the number corresponding to the row you want to drop your token in (or 8 to exit)")
    print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
  

# Main
# Creating the blank board
col = [["| - " for i in range(0, 6)] for j in range(0, 7)]

# Let's find out who our players are.....
print("Welcome to Connect 4! Whoever goes first uses 'X', and whoever else plays uses 'O'. Enjoy the game.")
player = ["", ""]
print("Who goes first (uses X)?")
player[0] = input()
print("Who goes last (uses O)?")
player[1] = input()

# initial board render
renderBoard(col)

# list to keep track of the token position
gravity = [0] * (8)

# variable to store the move counter
moves = 0

# variables to store tokens and player names when needed
token = ""
pindex = 0

# Variable to determine what space in the board to change
status = 0

# Main game loop
while moves < 42:
    # Variable for what the player enters
    columnChoice = -1

    # decide token
    pindex = 1 - (moves + 1) % 2
    if pindex != 0:
        token = "O"
    else:
        token = "X"

    # prompt for input
    displayPrompt(player, pindex, token)
    columnChoice = int(input())

    # validate choice
    while columnChoice < 1 or columnChoice > 8:
        print("Input invalid, try again")
        displayPrompt(player, pindex, token)
        columnChoice = int(input())

    # validates whether the column is full or not
    status = gravity[columnChoice - 1]
    while status > 5:
        status = 0
        columnChoice = -1
        print("Column full, try again")
        displayPrompt(player, pindex, token)
        columnChoice = int(input())
        while columnChoice < 1 or columnChoice > 8:
            print("Input invalid, try again")
            displayPrompt(player, pindex, token)
            columnChoice = int(input())
        status = gravity[columnChoice - 1]

    # Changes the token according to player, column choice and status, or exits the game
    if columnChoice < 8:
        col[columnChoice - 1][status] = "| " + token + " "
        # Changes the gravity setting for the next move
        gravity[columnChoice - 1] += 1
        renderBoard(col)
        win = check4Winner(col, token)
        #win = False
        if win == True:
            print(player[pindex] + " won the game!")
            moves = 42
        if moves == 41:
            print("The game is a draw!")
        moves += 1
    else:
        print("Exiting game.....")
        moves = 42
print("Oh, so the game's over? cool.")
