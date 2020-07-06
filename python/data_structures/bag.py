"""Chapter 1 - bag."""


class Bag:
    _items = []

    def add(self, item):
        self._items.append(item)

    def size(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0

    def __iter__(self):
        return iter(self._items)


if __name__ == '__main__':

    bag = Bag()

    bag.add(5)
    bag.add(7)
    bag.add(4)
    bag.add(9)
    bag.add(2)
    bag.add(4)
    bag.add(6)
    for x in bag:
        print(x)
