'''
Given two different positions on a chess board, find the least number of moves it would take a knight to get from one to the other. The positions will be passed as two arguments in algebraic notation. For example, knight("a3", "b5") should return 1.

The knight is not allowed to move off the board. The board is 8x8.

For information on knight moves, see https://en.wikipedia.org/wiki/Knight_%28chess%29

For information on algebraic notation, see https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29

(Warning: many of the tests were generated randomly. If any do not work, the test cases will return the input, output, and expected output; please post them.)




This approach ultimately failed, would be better for a more complex case but for an 8x8 grid the easiest way is to progress every tree simultaneously not try on at a time algorithmically.
'''



def swap_notation(point):
    return chr(point[0]+96)+str(point[1])

MOVE_LIST = [[-2,-1],[-2,1],[2,-1],[2,1],[-1,-2],[-1,2],[1,-2],[1,2]]
SOLVED_RANK = 5**.5
ADJACENT_RANK = [1.0, 2**.5]

def pythag(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**.5

def gen_next_points(p):
    return [(move[0] + p[0], move[1] + p[1]) for move in MOVE_LIST if 0 < move[0] + p[0] < 9 and 0 < move[1] + p[1] < 9]

def solve(matrix, visited_points, end):
    if not matrix:
        return
    for rank, point in matrix:
        if rank == SOLVED_RANK:
            print(swap_notation(point))
            return 1
        visited_points.add(point)
        new_matrix = sorted([[pythag(new_p1,end),new_p1] for new_p1 in gen_next_points(point) if (new_p1 not in visited_points) and (pythag(new_p1,end) < rank) and (pythag(new_p1, end) not in ADJACENT_RANK)])
        ans = solve(new_matrix, visited_points, end)
        if isinstance(ans, int):
            print(swap_notation(point))
            return ans + 1
    print(matrix)
    for rank, point in matrix:
        print(point)
        return knight(swap_notation(point),swap_notation(end),visited_points)
    return

def knight(p1, p2, visited_points = {(0,0)}):
    print(f"{p1}->{p2}")
    start, end = (ord(p1[0])-96, int(p1[1])), (ord(p2[0])-96, int(p2[1]))
    if pythag(start,end) == SOLVED_RANK:
        return 1
    visited_points.add(start)
    new_p1_matrix = sorted([[pythag(new_p1,end),new_p1] for new_p1 in gen_next_points(start)])
    return solve(new_p1_matrix, visited_points, end) + 1



# print(knight("a3","b5") == 1)
# print(knight("a3","e3") == 2)
# print(knight("b5","a3") == 1)
# print(knight("a1","c1") == 2)
# print(knight("a1","f4") == 4)
# print(knight("a1","f7") == 5)
# print(knight("a1","f3") == 3)
print(knight("a6","h6") == 5)
# print(knight("b2","c7") == 4)
# print(knight("c2","d7") == 4)


# columns = [chr(i) for i in range(ord("a"),ord("h")+1)]
# rows = [str(i) for i in range(1,9)]
# for start_row in rows:
#     for start_column in columns:
#         for row in rows:
#             for column in columns:
#                 if rows == start_row and columns == start_column:
#                     continue
#                 try:
#                     knight(start_column+start_row, column+row)
#                 except Exception as e:
#                     print(e)
#                     print(start_column+start_row+"->"+column+row)


