class Hash_Table:
	def __init__(self, size):
		self.size = size
		hash_table = [None] * self.size

	def insert(self, item_to_append):
		slot_index = self.hash()

	def hash(self, item_to_append):
		assert(type(item_to_append) is IntType)
		return int(item_to_append)


def main():
	pass

if __name__ == '__main__':
	main()