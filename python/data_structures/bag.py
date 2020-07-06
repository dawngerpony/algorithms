"""Chapter 1 - bag."""


class Bag:
    """ An implementation of a bag using lists.
    """

    def __init__(self, lst=None):
        self._items = lst if lst else []

    def add(self, item):
        """ Add an item to the bag.
        """
        self._items.append(item)

    def is_empty(self):
        """ Return True if the bag is empty.
        """
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __repr__(self):
        return f"Bag({self._items})"


if __name__ == '__main__':

    bag = Bag()
    assert len(bag) == 0

    bag.add(5)
    bag.add(7)
    bag.add(4)
    bag.add(9)
    bag.add(2)
    bag.add(4)
    bag.add(6)
    assert len(bag) == 7
    print(bag)
    for x in bag:
        print(x)
