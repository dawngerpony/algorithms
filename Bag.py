# Chapter 1 - bag
class Bag:
	items = []

	def add(self, item):
		self.items.append(item)

	def size(self):
		return len(self.items)

if __name__ == '__main__':
	print "hello"

	bag = Bag()

	bag.add(5)
	bag.add(7)
	bag.add(4)
	bag.add(9)
	bag.add(2)
	bag.add(4)
	bag.add(6)
	for x in bag.items:
		print x
