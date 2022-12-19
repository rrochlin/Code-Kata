# https://www.codewars.com/kata/55171d87236c880cea0004c6/train/python
'''
fill in first 0 with a 1 -> check if valid:
valid -> proceed to next 0, fill with 1 -> check if valid
invalid -> try with 2 -> check if valid
once 9 is invalid -> go back to last insertion and increase
recurse until solved.

this method needs to keep track of all inputs, so will need to preserve og board and get the difference of each, or just an array of indices of the 0's
will need to check for duplicate values not 0 in the local grid, and the local rows -> total of 9 different grids
'''
import numpy as np
grid_mask = np.array([[i//3+j//3*3 for i in range(9)] for j in range(9)])
one_to_nine = set(i for i in range(1,10))

def valid_options(point : tuple, board : np.array):
    '''
    param - point = (row, column) : tuple with the associated row and column of the point
    param - board = np.array(list()) : 9 x 9 nested list of the current state of the sudoku board
    return - options = list() : returns all remaining values this point can be
    '''
    (row, column) = point
    checks = set(board[row])
    checks.update(set([row[column] for row in board]))
    grid = row//3*3 + column//3
    checks.update(set(board[grid_mask==grid]))
    options = one_to_nine.difference(checks)
    return options

def depth_first(board, board_positions, cell, open_cells, options):
    '''
    param - board = np.array : 9 x 9 nested list of the current state of the sudoku board
    param - board_postions = list(tuple) : list of tuples that correspond in order to the empty spots in the puzzle
    param - cell = int : current position in the board_positions list
    param - open_cells = int : length of board_positions list
    return - board = np.array : board param with the solution
    '''
    if cell == open_cells: return board
    point = board_positions[cell]
    if list(board[1]) == [7, 1, 3, 4, 0, 6, 0, 0, 0]:
        print("here")
    for option in options:
        board[point[0]][point[1]] = option
        try:
            new_options = valid_options(board_positions[cell+1], board)
        except:
            return board
        result = None
        if new_options: 
            result = depth_first(board, board_positions, cell + 1, open_cells, new_options)
        if isinstance(result, np.ndarray):
            return result
        board[point[0]][point[1]] = 0
    return None


def solve(board):
    board = np.array(board)
    board_positions = [(j,i) for j in range(9) for i in range(9) if board[j][i] == 0]
    options = valid_options(board_positions[0], board)
    final_board = depth_first(board, board_positions, cell = 0, open_cells = len(board_positions), options = options)
    return final_board.tolist()


puzzle = [
            [9, 0, 0, 0, 8, 0, 0, 0, 1],
            [0, 0, 0, 4, 0, 6, 0, 0, 0],
            [0, 0, 5, 0, 7, 0, 3, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 4, 0],
            [4, 0, 1, 0, 6, 0, 5, 0, 8],
            [0, 9, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 7, 0, 3, 0, 2, 0, 0],
            [0, 0, 0, 7, 0, 5, 0, 0, 0],
            [1, 0, 0, 0, 4, 0, 0, 0, 7]
        ]
solution = [
            [9, 2, 6, 5, 8, 3, 4, 7, 1],
            [7, 1, 3, 4, 2, 6, 9, 8, 5],
            [8, 4, 5, 9, 7, 1, 3, 6, 2],
            [3, 6, 2, 8, 5, 7, 1, 4, 9],
            [4, 7, 1, 2, 6, 9, 5, 3, 8],
            [5, 9, 8, 3, 1, 4, 7, 2, 6],
            [6, 5, 7, 1, 3, 8, 2, 9, 4],
            [2, 8, 4, 7, 9, 5, 6, 1, 3],
            [1, 3, 9, 6, 4, 2, 8, 5, 7]
        ]

# grid = 2
# [[col for col_idx,col in enumerate(row)] for (row_idx, row) in enumerate(puzzle) if grid_mask[row_idx,col_idx] == grid]]
# [[puzzle[i][j] for j,val in enumerate(row) if grid_mask[i][j] == grid] for i,row in enumerate(grid_mask) if grid in row]

print(solve(puzzle) == solution)