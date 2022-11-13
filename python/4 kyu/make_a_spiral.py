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
    print(n,size)
    print(0+(size-n)//2)
    print((size-n)//4)
    print(-(size-n)//2-1)
    row = 0+(size-n)//2
    start = (size-n)//4
    end = -(size-n)//2-1
    output = [1]*(n-n%2)
    spiral[row][start:end] = output
    return spiral
def down(spiral, n, size):
    return spiral
def left(spiral, n, size):
    return spiral
def up(spiral, n, size):
    return spiral
action = [right,down,left,up]

def spiralize(size):
    spiral = np.array([[0]*size for _ in range(size)])
    # 1 - size
    for i in range(1,size+1)[::-1]:
        spiral = action[(size-i)%4](spiral, i, size)

        # for _ in range(i + i%2):
        #     spiral[0][i] = 1
        #     spiral[i][size-1] = 1
        #     spiral[size-1][size-1-i] = 1
    # for i in range(size-1,1,-1):
    #     spiral[i][0] = 1
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


pprint(spiralize(7))