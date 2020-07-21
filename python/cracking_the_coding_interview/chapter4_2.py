""" Given a sorted (increasing order) array with unique integer elements, write an algorithm
    to create a binary search tree with minimal height.
"""

class Node:
    def __init__(self, value, depth=0):
        super().__init__()
        self.value = str(value)
        self.left = None
        self.right = None
        self.depth = depth

def in_order(node):
    """ Print the tree in-order (left, value, right). """
    if node:
        in_order(node.left)
        print(node.value, end=",")
        in_order(node.right)

def pre_order(node):
    """ Print the tree in pre-order (value before children). """
    if node:
        print(node.value, end=",")
        in_order(node.left)
        in_order(node.right)

def post_order(node):
    """ Print the tree in post-order (value after children). """
    if node:
        in_order(node.left)
        in_order(node.right)
        print(node.value, end=",")

def print_tree_traverse_pre_order(node, padding="", pointer=""):
    """ This does not work. I am not sure why. Ported from https://www.baeldung.com/java-print-binary-tree-diagram."""
    s1 = ""
    if node:
        print(f"Node: {node.value}")
        s1 += padding
        s1 += pointer
        s1 += node.value
        s1 += "\n"
        # print(s1)

        padding = "| "
        pointer_right = "└──"
        pointer_left = "├──" if node.right is not None else "└──"
        print(f"pointer_left for {node.value} = {pointer_left}")
        s1 += print_tree_traverse_pre_order(node.left, padding, pointer_left)
        s1 += print_tree_traverse_pre_order(node.right, padding, pointer_right)
    return s1


def minimal_tree(lst, depth=0, debug=False):
    """ This algorithm seems to work ok, if I could figure out a way to print it properly.
    """
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return Node(lst[0], depth=depth)
    mid = len(lst)//2
    node = Node(lst[mid], depth=depth)
    left = lst[0:len(lst)//2]
    right = lst[len(lst)//2+1:]
    if debug:
        print(f"mid: {mid}, value: {node.value}, left={left}, right={right}")
    node.left = minimal_tree(left, depth=depth+1)
    node.right = minimal_tree(right, depth=depth+1)
    return node

def bfs(initial):
    """ Breadth-first search of a binary tree.
    """
    visited = []
    queue = [initial]
    s = ""
    while queue:
        node = queue.pop(0)
        if node and node not in visited:
            print(f"Appending {node.value}")
            visited.append(node)
            s += node.value
            s += " "
            children = [node.left, node.right]
            for child in children:
                queue.append(child)
    for node in visited:
        print(f"{node.value} ({node.depth})")

def minimal_bst(lst, start=0, end=None):
    """ This algorithm DOES NOT WORK. Either the book has an error
        or I have no figured out how to port it properly from Java to Python.
    """
    if end is None:
        end = len(lst) - 1
    if end <= start:
        print("None")
        return None
    mid = (start + end) // 2
    node = Node(lst[mid])
    print(f"value={node.value}, start={start}, mid-1={mid - 1}, mid+1={mid + 1}, end={end}")
    print(f"left of {node.value} ({lst[0:mid]}):")
    node.left = minimal_bst(lst, 0, mid - 1)
    print(f"right of {node.value} ({lst[mid+1:]}):")
    node.right = minimal_bst(lst, mid + 1, end)
    return node

# root = minimal_tree([1,2,3,4,5,6,7,8,9,10])
root = minimal_tree([1,2,3,4,5])
print("In-order: ")
in_order(root)
print("\nPre-order: ")
pre_order(root)
print("\nPost-order: ")
post_order(root)
print("\nBFS: ")
bfs(root)
# assert isinstance(root, Node)
# s = print_tree_traverse_pre_order(root)
# print(s)
# lst = [1,2,3,4,5,6,7,8,9,10]
# lst = [1,2,3,4,5]
# print(lst)
# root = minimal_bst(lst)
