# https://www.codewars.com/kata/571a7c0cf24bdf99a8000df5/train/python
import pandas as pd
import numpy as np


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

    def __gt__(self, other):
        # added these methods for heapq merge
        return self.root > other.root

    def __lt__(self, other):
        # added these methods for heapq merge
        return self.root < other.root

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
    length = len(node_list)+1
    cost_table = pd.DataFrame(data=np.zeros((length, length), dtype=np.uint32), index=range(1, length+1))
    node_table = pd.DataFrame(data=np.nan, index=range(1, length+1), columns=range(0, length))
    for idx, node in enumerate(node_list):
        cost_table.at[idx+1, idx+1] = node.weight
        node_table.at[idx+1, idx+1] = node.value
    for start in range(1, length-1):
        for idx in range(1, length-start):
            cost_list = []
            for i in range(start+1):
                val = cost_table.at[idx, idx+i-1] + cost_table.at[idx+i+1, idx+start]
                cost_list.append((val, node_list[idx + i - 1].value))
            min_cost, root = min(cost_list)
            increased_cost = sum([node.weight for node in node_list[idx-1:idx+start]])
            cost_table.at[idx, idx+start] = min_cost + increased_cost
            node_table.at[idx, idx+start] = root

    print(cost_table)  #.iloc[:10, :10])
    print(node_table)  #.iloc[:10, :10])
    # cost_table.at[row, column]


a = Node('A', 10)
b = Node('B', 2)
c = Node('C', 4)
d = Node('D', 9)
e = Node('E', 8)
tree_abcde2 = Tree(d, Tree(a, None, Tree(c, Tree(b), None)), Tree(e))
# print(tree_abcde2)
# print(cost(tree_abcde2))


def check(x, y):
    print("result: ", x, " cost: ", cost(x))
    print("answer: ", y)
    print(x == y)
    print()
    print()


# check(make_min_tree([a]), '[A:10]')
# check(make_min_tree([a, b]), '[_ A:10 [B:2]]')
# check(make_min_tree([a, b, c]), '[_ A:10 [[B:2] C:4 _]]')
# correct = '[[_ A:10 [[B:2] C:4 _]] D:9 [E:8]]'
# result = make_min_tree([a, b, c, d, e])
# print("result: ", result, " cost: ", cost(result))
# print("answer: ", correct, " cost: ", cost(tree_abcde2))
# print(result == correct)

node_list = [
    Node("AGL", 63558),
    Node("AJY", 92939),
    Node("ALD", 68666),
    Node("AOU", 55384),
    Node("AXJ", 68745),
    Node("AXX", 15716),
    Node("CBX", 82270),
    Node("CCX", 29232),
    Node("CFJ", 43977),
    Node("CHU", 11403),
    Node("CMD", 79929),
    Node("CRB", 39788),
    Node("CVY", 26105),
    Node("DBD", 2319),
    Node("DCR", 99534),
    Node("DLV", 84675),
    Node("DSX", 40884),
    Node("EPK", 39181),
    Node("ESQ", 92308),
    Node("FFY", 66830),
    Node("FOM", 16286),
    Node("FQE", 43854),
    Node("FXB", 78435),
    Node("GDD", 128),
    Node("GHF", 87898),
    Node("GIE", 64680),
    Node("GJH", 36879),
    Node("GSL", 10382),
    Node("GWC", 67483),
    Node("HHL", 11876),
    Node("HLJ", 66246),
    Node("HQQ", 15461),
    Node("HYR", 96279),
    Node("IHQ", 33764),
    Node("IUM", 16104),
    Node("IZX", 93845),
    Node("JJP", 98416),
    Node("JKY", 18541),
    Node("KBM", 34251),
    Node("KEY", 27505),
    Node("KGG", 39501),
    Node("KGN", 86207),
    Node("KJA", 82983),
    Node("KNP", 85206),
    Node("LMY", 46791),
    Node("LRI", 85848),
    Node("LWT", 53981),
    Node("MFT", 12251),
    Node("MRB", 1913),
    Node("NAY", 53087),
    Node("NRA", 94153),
    Node("NXP", 46524),
    Node("NYX", 22916),
    Node("OBC", 52752),
    Node("OBY", 46029),
    Node("ODJ", 62971),
    Node("OVP", 56558),
    Node("PCF", 50446),
    Node("PTZ", 29558),
    Node("PVR", 64787),
    Node("QAH", 73305),
    Node("QYF", 49216),
    Node("RHB", 85992),
    Node("RLW", 92569),
    Node("ROV", 80724),
    Node("SCC", 92333),
    Node("SGN", 63161),
    Node("SOG", 54060),
    Node("SSS", 44840),
    Node("TFY", 40060),
    Node("TLB", 10803),
    Node("TWR", 32887),
    Node("TZI", 94279),
    Node("UEV", 31119),
    Node("UKG", 44716),
    Node("ULR", 76830),
    Node("VAB", 65810),
    Node("VJF", 58050),
    Node("VLE", 21798),
    Node("VWP", 80918),
    Node("VYP", 52155),
    Node("WDE", 44576),
    Node("WHS", 57098),
    Node("WTN", 85932),
    Node("XED", 81746),
    Node("XFF", 47653),
    Node("XKE", 16648),
    Node("XPA", 49553),
    Node("XQD", 35026),
    Node("YAJ", 15048),
    Node("YEG", 36880),
    Node("YJO", 28252),
    Node("YXT", 90921),
    Node("ZET", 13282),
    Node("ZHQ", 32177),
    Node("ZNA", 18419),
    Node("ZNT", 63046),
    Node("ZOY", 65301),
    Node("ZYP", 56786),
]

print(make_min_tree(node_list))

