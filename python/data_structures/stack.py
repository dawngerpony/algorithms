""" A (very lazy) implementation of a stack in Python 3. """


class Stack:
    """ A (very lazy) implementation of a stack in Python 3. """
    collection = []

    def push(self, element):
        """ Add an item onto the top of the stack. """
        self.collection.append(element)

    def pop(self):
        """ Remove the item at the top of the stack. """
        return self.collection.pop()


if __name__ == "__main__":
    items = ["red", "blue", "green"]

    stack = Stack()

    for item in items:
        stack.push(item)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    try:
        print(stack.pop())
    except IndexError as err:
        print(f"Error: {err}")
