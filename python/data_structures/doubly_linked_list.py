""" An implementation of a doubly linked list. """


class Node:
    """ A node in the list. """

    def __init__(self, item, next_node=None, prev_node=None):
        self._item = item
        self._next = next_node
        self._prev = prev_node

    def link(self, next_node):
        """ Link the next node to the current node. """
        self._next = next_node
        next_node.link(self)

    def next(self):
        """ Get the next node. """
        return self._next

    def prev(self):
        """ Get the previous node. """
        return self._prev

    def __str__(self):
        return str(self._item)


if __name__ == "__main__":
    node1 = Node("red")
    node2 = Node("blue")
    node3 = Node("green")

    node1.link(node2)
    node2.link(node3)

    node = node1
    while node is not None:
        print(node)
        node = node.next()

    node = node3
    while node is not None:
        print(node)
        node = node.prev()
