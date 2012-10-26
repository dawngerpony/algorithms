# queue.py

# An implementation of a queue. Very similar to the queue except it pops
# the first element off the list instead of the last.

class Queue:

	items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop(0)

if __name__ == "__main__":
	item1 = "red"
	item2 = "blue"
	item3 = "green"

	queue = Queue()

	queue.push(item1)
	queue.push(item2)
	queue.push(item3)

	print queue.pop()
	print queue.pop()
	print queue.pop()

	# This last one generates an error.
	print queue.pop()
