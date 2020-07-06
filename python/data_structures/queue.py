""" An implementation of a queue. Very similar to the queue except it pops
    the first element off the list instead of the last.
"""


class Queue:
    """ Simple queue implementation using lists.
    """
    items = []

    def push(self, item):
        """ Add an item to the end of the queue."""
        self.items.append(item)

    def pop(self):
        """ Remove an item from the front of the queue."""
        return self.items.pop(0)


if __name__ == "__main__":
    ITEM1 = "red"
    ITEM2 = "blue"
    ITEM3 = "green"

    queue = Queue()

    queue.push(ITEM1)
    queue.push(ITEM2)
    queue.push(ITEM3)

    print(queue.pop())
    print(queue.pop())
    print(queue.pop())

    # This last one generates an error.
    print(queue.pop())
