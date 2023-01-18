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
        self.mystery_ship_length = 0

    def add_to_ship_length(self):
        self.mystery_ship_length += 1
        if self.mystery_ship_length > 4:
            return False

    def add_ship(self):
        ship_length = self.mystery_ship_length
        if ship_length < 1:
            raise Exception("tryed to add ship of length 0")
        elif ship_length == 1:
            self.submarines -= 1
        elif ship_length == 2:
            self.destroyers -= 1
        elif ship_length == 3:
            self.cruisers -= 1
        elif ship_length == 4:
            self.battleships -= 1
        self.mystery_ship_length = 0
        if any(prop < 0 for prop in dict(vars(self)).values()):
            raise Exception(f"too many ships requests {vars(self)}")

    def confirm_no_more_ships(self):
        return not any(not (ship == 0) for ship in dict(vars(self)).values())


def explore(field: list, coordinates: list, ships: Ships):
    if len(coordinates) == 0:
        return True
    (x, y) = coordinates[0]
    if field[y][x]:
        traverse(field, (x, y), coordinates, ships)
        ships.add_ship()
        return explore(field, coordinates, ships)
    return explore(field, coordinates[1:], ships)


def traverse(field: list, start: tuple, coordinates: list, ships: Ships):
    (x, y) = start
    coordinates.pop(coordinates.index(start))
    ships.add_to_ship_length()
    surrounding_points = [
        (x+1, y) if x < 9 else None,
        (x-1, y+1) if x > 0 and y < 9 else None,
        (x, y+1) if y < 9 else None,
        (x+1, y+1) if x < 9 and y < 9 else None
    ]
    surrounding_points = list(
        filter(lambda item: item is not None, surrounding_points))
    surrounding_values = [field[j][i] for (i, j) in surrounding_points]
    if sum(surrounding_values) > 1:
        raise Exception("ships touching")
    if sum(surrounding_values) == 1:
        next_point = surrounding_points[surrounding_values.index(1)]
        coordinates = traverse(field, next_point, coordinates, ships)
    return coordinates


def validate_battlefield(field: list):
    coordinates = [(x, y) for y in range(0, len(field[0]))
                   for x in range(len(field))]
    ships = Ships()
    try:
        explore(field, coordinates, ships)
    except Exception as e:
        print(e)
        return False
    return ships.confirm_no_more_ships()


battleField = [[0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
               [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

assert validate_battlefield(battleField) is False
