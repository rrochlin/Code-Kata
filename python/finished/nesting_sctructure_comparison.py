'''
Complete the function/method (depending on the language) to return true/True when its argument is 
an array that has the same nesting structures and same corresponding length of nested arrays as the 
first array.


'''

def same_structure_as(original,other):
    original_type, other_type = type(original), type(other)
    if original_type != other_type:
        return False
    if original_type == other_type == list and len(original) != len(other):
        return False
    for og, new in zip(original, other):
        if isinstance(og, list) != isinstance(new, list):
            return False
        if isinstance(og, list) and (len(og) != len(new) or not same_structure_as(og,new)):
            return False
    return True


# should return True
print(same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] ))
print(same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] ))
# should return True
print(same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] ))

# should return False
print(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] ))
print(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] ))


# should return False
print(same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] ))
print(same_structure_as([1,[1,1]], [2,[2]]))
print(same_structure_as([-4, 2] , [9, -4, 12, -10, -1, -18, 15, -1, -2, [-1, 17], -14, 15, -7, -11]))