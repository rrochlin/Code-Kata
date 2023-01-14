# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python

'''
There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 
4 submarines (size 1). Any additional ships are not allowed, as well as missing ships. Each ship 
must be a straight line, except for submarines, which are just single cell.

plan:
create an ordered list of all the coordinates to visit that is ordered left -> right, top -> bottom
iterate over the list, scanning for ones
when we hit a one, explore the matrix looking for the rest of it
    record its position
    mark off its type
    remove explored points from the list
    return from function with false if we find a violation

    valid configurations should only have points in one plane around the ship, or all 0's
    


VIOLATIONS:
    a yielded shape that is not 1D
    finding a shape that is already accounted for
'''

class Ships():
    def __init__(self):
        self.battleships = 1
        self.cruisers = 2
        self.destroyers = 3
        self.submarines = 4
    def add_ship(self, ship_length):
        if ship_length == 1:
            self.submarines -= 1
        elif ship_length == 2:
            self.destroyers -=1
        elif ship_length == 2:
            self.destroyers -=1
        elif ship_length == 2:
            self.destroyers -=1
        if any(prop < 0 for prop in vars(self)):
            return False


def explore(field, coordinates, ships):
    if len(coordinates) == 0:
        return True
    if coordinates[0]:
         traverse(coordinates[1:])
    return (coordinates[1:])
    
def traverse(field, coordinates, ships):
    start = coordinates[0]
    coordinates.pop(coordinates.index(start))
    x = start[0]
    y = start[1]
    # check for points to the right first
    while x < 10:
        x+=1
        coordinates.pop(coordinates.index((x, start[1])))
        if 
    x = start[0]
    # next check for points below
    
'''There must be single battleship (size of 4 cells), 
2 cruisers (size 3), 3 destroyers (size 2) and 
4 submarines (size 1)'''
def validate_battlefield(field):
    coordinates = [(x,y) for x in range(0,len(field[0])) for y in range(len(field))]
    ships = {"battleship": {"limit": 1, "seen": 0},
             "cruiser": {"limit": 2, "seen": 0},
             "destroyer": {"limit": 3, "seen": 0},
             "sub": {"limit": 4, "seen": 0},
    }
    return explore(field, coordinates, ships)

battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(validate_battlefield(battleField))