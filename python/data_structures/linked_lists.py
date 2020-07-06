""" Implementations of singly and doubly linked lists. """


class SinglyLinkedList:
    """ A singly linked list. """

    def __init__(self, value=None):
        self._head = self.Node(value)

    def insert(self, value):
        new_node = self.Node(value)
        curr = self._head
        while curr.next():
            curr = curr.next()
        curr.next(new_node)

    def search(self, value):
        curr = self._head
        found = False
        while curr and not found:
            if curr.value() == value:
                found = True
            else:
                curr = curr.next()
        return curr if found else None

    def __len__(self):
        curr = self._head
        count = 0
        while curr:
            curr = curr.next()
            count += 1
        return count

    class Node:
        """ A node in the list. """

        def __init__(self, value=None, next_node=None):
            self._value = value
            self._next = next_node

        def next(self, next_node=None):
            """ Set the next item, or return it. """
            if next_node:
                self._next = next_node
            return self._next

        def value(self):
            """ Get the value of the node. """
            return self._value

        def __str__(self):
            return str(self._value)


class DoublyLinkedList:
    """ A doubly linked list. """

    def __init__(self, value=None):
        self._head = self.Node(value)

    def insert(self, value):
        pass

    class Node:
        """ A node in a doubly linked list. """

        def __init__(self, item, next_node=None, prev_node=None):
            self._value = item
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
            return str(self._value)
