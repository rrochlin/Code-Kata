'''
Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000
and with the size 10:

0000000000
.........0
00000000.0
0......0.0
0.0000.0.0
0.0..0.0.0
0.0....0.0
0.000000.0
0........0
0000000000
Return value should contain array of arrays, of 0 and 1, with the 
first row being composed of 1s. For example for given size 5 result
should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch 
to itself.
'''
from pprint import pprint
import numpy as np

def right(spiral, n, size):
    row = (n//4)*2+1
    col_start = 0 if n == 0 else (n//4)*2-1
    col_end = -(n//4)*2-1
    spiral[row][col_start:col_end] = [0]*(size+col_end-col_start)
    return spiral
def down(spiral, n, size):
    row_start = (n//4)*2 + 1
    row_end = -(n//4)*2 - 1
    col = -(n//4)*2 -2
    for i in range(row_start,size+row_end):
        spiral[i][col] = 0
    return spiral
def left(spiral, n, size):
    row = -((n//4)*2+2)
    col_start = 1 if n == 2 else (n//4)*2+1
    col_end = -(n//4)*2-1
    spiral[row][col_start:col_end] = [0]*(size+col_end-col_start)
    return spiral
def up(spiral, n, size):
    col = 1 if n == 2 else (n//4)*2+1
    row_end = -((n//4)*2+1)
    row_start = ((n+1)//4)*2+1
    for i in range(row_start,size+row_end):
        spiral[i][col] = 0
    return spiral

action = [right,down,left,up]

def spiralize(size):
    spiral = np.array([[1]*size for _ in range(size)])
    for i in range(0,size-1):
        spiral = action[i%4](spiral, i, size)
    return spiral

'''
%4 - control direction of growth
    0 - right
    1 - down
    2 - left
    3 - up
%2 - spiral of size 10 should grow like:
        10, 10, 8, 8, 6, 6, 4, 4, 2, 2
spiral will have equal numbers of growth as size
'''


pprint(spiralize(10))
pprint(spiralize(5))