# LinkedList.py

class Node:
	item = None
	next = None

	def __init__(self, item):
		self.item = item

if __name__ == "__main__":
	node1 = Node("red")
	node2 = Node("blue")
	node3 = Node("green")

	node1.next = node2
	node2.next = node3

	node = node1
	while(node != None):
		print node.item
		node = node.next
