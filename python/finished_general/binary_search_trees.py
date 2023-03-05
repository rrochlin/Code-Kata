# https://www.codewars.com/kata/571a551a196bb0567f000603/train/python

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
        if not self or not other:
            return not self and not other
        return self.root == other.root and self.right == other.right and self.left == other.left

    def __ne__(self, other):
        if not self or not other:
            return not (not self and not other)
        return self.root != other.root or self.right != other.right or self.left != other.left


class Node(object):

    def __init__(self, value, weight=1):
        self.value = value
        self.weight = weight

    def __str__(self):
        return str(self.value)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value


tree1 = Tree(Node('B'), Tree(Node('A')), Tree(Node('C')))
tree2 = Tree(Node('B'), None, Tree(Node('C')))
print(tree1 != tree2)
