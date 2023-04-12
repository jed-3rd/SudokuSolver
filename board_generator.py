import random
import copy
from solver import solve


def validator(board, num, pos):
    row = pos[0]
    col = pos[1]
    #If position has already been filled it's not a valid clue
    if board[row][col] != 0:
        return False
    #If position is empty, validate placement
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


def generator():
    new_board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    i = 0
    while i < 17:
        #Randomly selects a location on the board to place starter
        rand_element_row = random.randint(0,8)
        rand_element_col = random.randint(0,8)
        #Randomly selects the starter element
        rand_element = random.randint(1,9)
        #Check to see if the starter element is a valid placement at location
        if validator(new_board, rand_element,(rand_element_row, rand_element_col)):
            #If starter element / clue can be placed increment clue counter and place
            new_board[rand_element_row][rand_element_col] = rand_element
            i += 1
    start_board = copy.deepcopy(new_board)
    #If generated board cannot be solved, start generator over
    if solve(new_board) == False:
        start_board = generator()
    #Return generated board
    return start_board, new_board
