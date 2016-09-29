class Stack:
	def __init__(self):
		self.array = []

	def push(self, item):
		self.array[len(self.array) - 1] = char

	def pop(self):
		item = self.array[len(self.array) - 1]
		return item

	def peek(self):
		if self.size() == 0:
			return None
		else:
			item = self.array[len(self.array) - 1]
			return item

	def size(self):
		return len(self.array)

if __name__ == '__main__':
	main()