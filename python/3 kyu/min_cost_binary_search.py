# https://www.codewars.com/kata/571a7c0cf24bdf99a8000df5/train/python

class Tree(object):

    def __init__(self, root, left=None, right=None):
        assert root and type(root) == Node
        if left:
            assert type(left) == Tree and left.root < root
        if right:
            assert type(right) == Tree and root < right.root

        self.left = left
        self.root = root
        self.right = right

    def is_leaf(self):
        return not (self.left or self.right)

    def __str__(self):
        if self.is_leaf():
            return f"[{str(self.root)}]"
        else:
            left = str(self.left) if self.left else "_"
            right = str(self.right) if self.right else "_"
            return f"[{left} {str(self.root)} {right}]"

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return not (self == other)


class Node(object):

    def __init__(self, value, weight=1):
        self.value = value
        self.weight = weight

    def __str__(self):
        return '%s:%d' % (self.value, self.weight)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value


def cost(tree, depth=1):
    '''
    Returns the cost of a tree which root is depth deep.
    '''
    result = tree.root.weight * depth
    if tree.left:
        result += cost(tree.left, depth + 1)
    if tree.right:
        result += cost(tree.right, depth + 1)
    return result


def make_min_tree(node_list):
    '''
    node_list is a list of Node objects
    Pre-cond: len(node_list > 0) and node_list is sorted in ascending order
    Returns a minimal cost tree of all nodes in node_list.
    '''
    tempTree = Tree(node_list[0])
    for node in node_list[1:]:
        
    return tempTree


a = Node('A', 10)
b = Node('B', 2)
c = Node('C', 4)
d = Node('D', 9)
e = Node('E', 8)
tree_abcde2 = Tree(d, Tree(a, None, Tree(c, Tree(b), None)), Tree(e))
print(tree_abcde2)
print(cost(tree_abcde2))
print(make_min_tree([a, b, c, d, e]))
'[[_ A:10 [[B:2] C:4 _]] D:9 [E:8]]'
