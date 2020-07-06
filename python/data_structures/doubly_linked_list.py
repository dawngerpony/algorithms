# DoublyLinkedList.py

class Node:
    item = None
    next = None
    prev = None

    def __init__(self, item):
        self.item = item

    def link(self, next):
        self.next = next
        next.prev = self


if __name__ == "__main__":
    node1 = Node("red")
    node2 = Node("blue")
    node3 = Node("green")

    node1.link(node2)
    node2.link(node3)

    node = node1
    while (node != None):
        print(node.item)
        node = node.next

    node = node3
    while (node != None):
        print(node.item)
        node = node.prev
