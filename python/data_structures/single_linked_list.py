""" Singly linked list. """


class Node:
    """ A node in the list. """

    def __init__(self, item, next_item=None):
        self._item = item
        self._next = next_item

    def next(self, next_item=None):
        """ Set the next item, or return it. """
        if next_item:
            self._next = next_item
        return self._next

    def __str__(self):
        return str(self._item)


def main():
    """ Basic demonstration of the linked list. """
    node1 = Node("red")
    node2 = Node("blue")
    node3 = Node("green")

    node1.next(node2)
    node2.next(node3)

    node = node1
    while node is not None:
        print(node)
        node = node.next()


if __name__ == "__main__":
    main()
