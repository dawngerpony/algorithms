""" A (very lazy) implementation of a stack in Python 3.
"""


class Stack:

	collection = []

	def push(self, el):
		self.collection.append(el)

	def pop(self):
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
