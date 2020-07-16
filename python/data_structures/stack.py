""" The Stack data structure. """


class Stack:
    """ A (very lazy) implementation of a stack in Python 3. """
    items = []

    def push(self, item):
        """ Add an item onto the top of the stack. """
        self.items.append(item)

    def pop(self):
        """ Remove the item at the top of the stack. """
        return self.items.pop()
