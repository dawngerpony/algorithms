# stack.py

# An implementation of a stack.
# A little lazy because it uses Python lists under the hood,
# but it's a start. I should really do this in C instead.

class Stack:

	items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

if __name__ == "__main__":
	item1 = "red"
	item2 = "blue"
	item3 = "green"

	stack = Stack()

	stack.push(item1)
	stack.push(item2)
	stack.push(item3)

	print stack.pop()
	print stack.pop()
	print stack.pop()
	print stack.pop()
