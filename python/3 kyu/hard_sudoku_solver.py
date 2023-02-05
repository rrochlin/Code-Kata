# https://www.codewars.com/kata/55171d87236c880cea0004c6/train/python
'''
calculate valid_options for each square, put into grid or something
find a combonation of these that have 0 overlap?
'''
import numpy as np
grid_mask = np.array([[i//3+j//3*3 for i in range(9)] for j in range(9)])
one_to_nine = set(i for i in range(1, 10))


def valid_options(point: tuple, board: np.array):
    '''
    param - point = (row, column) : tuple with the associated row and column of the point
    param - board = np.array(list()) : 9 x 9 nested list of the current state of the sudoku board
    return - options = list() : returns all remaining values this point can be
    '''
    (row, column) = point
    checks = set(board[row])
    checks.update(set([row[column] for row in board]))
    grid = row//3*3 + column//3
    checks.update(set(board[grid_mask == grid]))
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
    if cell == open_cells:
        return board
    point = board_positions[cell]
    for option in options:
        board[point[0]][point[1]] = option
        try:
            new_options = valid_options(board_positions[cell+1], board)
        except Exception as e:
            print(e)
            return board
        result = None
        if new_options:
            result = depth_first(board, board_positions,
                                 cell + 1, open_cells, new_options)
        if isinstance(result, np.ndarray):
            return result
        board[point[0]][point[1]] = 0
    return None


def solve(board):
    board_numpy = np.array(board)
    board_positions = [(j, i) for j in range(9)
                       for i in range(9) if board[j][i] == 0]
    options = np.array([valid_options(point, board_numpy)
                       for point in board_positions])
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if (i, j) in board_positions:
                board[i][j] = list(options[board_positions.index((j, i))])
            else:
                board[i][j] = [col]
    number_of_combinations = [[len(i) for i in row] for row in board]
    number_of_combinations = np.prod(
        [np.prod([len(i) for i in row]) for row in board], dtype='object')
    i = 0
    while i < number_of_combinations:
        i += 1
    board = np.array(board)
    print(board)
    print(number_of_combinations)
    final_board = depth_first(board, board_positions, cell=0, open_cells=len(
        board_positions), options=options)
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

print(solve(puzzle) == solution)
