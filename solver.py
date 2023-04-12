#Finds first avaliable empty (or 0) on the board and return it's position
def find_empty_space(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            #If board location is 0 it is empty
            if board[i][j] == 0:
                return (i, j)  # row, column
    return None


#Checks to make sure the current board is a valid Sudoku Board
def validator(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        #Go through the row, if the number matches it is not valid
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(board)):
        #Go through the column, if the number matches it is not valid
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # Check square
    #Determine the column and row we are in (0-2) for each
    squ_x = pos[1] // 3
    squ_y = pos[0] // 3
    #Step through the given box checking for if the number matches
    for i in range(squ_y*3, squ_y*3 + 3):
        for j in range(squ_x * 3, squ_x*3 + 3):
            #If the number matches it is not valid
            if board[i][j] == num and (i,j) != pos:
                return False
    return True


#Recursively Solves the current board using backtracking
def solve(board):
    #Find empty space
    empty = find_empty_space(board)
    #If board is not empty it has been solved
    if not empty:
        return True
    else:
        #Get location of empty space
        row, col = empty
    for i in range(1,10):
        #Loop through 1-9 looking for the first valid number
        if validator(board, i, (row, col)):
            #Add valid solution into board
            board[row][col] = i
            #Recursive call with new value
            if solve(board):
                #If solve is true board has been solved
                return True
            board[row][col] = 0
    return False
