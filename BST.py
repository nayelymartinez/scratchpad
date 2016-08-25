class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def set_right(self, node):
		self.right = node
		return

	def set_left(self, node):
		self.left = node
		return

	def get_right(self):
		return self.right

	def get_left(self):
		return self.left

	def get_data(self):
		return self.data

class BST:
	def __init__(self):
		self.root = None
		self.size = 0

	def set_root(self, node):
		self.root = node
		return

	def get_root(self):
		return self.root

	def insert(self, data):
		if data is None:
			print("No object inserted [None].")
			return None
		to_insert = Node(data)
		if self.root is None:
			self.set_root(to_insert)
			print("new root inserted")
			return
		else:
			self.insert_node(self.root, to_insert)

	def insert_node(self, parent, node):
		if parent.get_data() >= node.get_data(): # Go left
			if parent.get_left() is None:
				parent.set_left(node)
				print("Node inserted as left")
				return
			else:
				parent = parent.get_left()
				self.insert_node(parent, node)
				print("Node goes left")
		else: # Go right
			if parent.get_right() is None:
				parent.set_right(node)
				print("Node inserted as right")
				return
			else:
				parent = parent.get_right()
				self.insert_node(parent, node)
				print("node goes right")

	def search(self, data):
		return self.search_node(self.root, data)

	def search_node(self, parent, data):
		# Case 1: It matches
		if parent.get_data() == data:
			return parent
		# Recurse!
		else:
			if parent.get_data() >= data: # Go left
				if parent.get_left() is not None:
					return self.search_node(parent.get_left(), data)
				else:
					# Case 2: It does not match anything
					return None
			else: # Go right
				if parent.get_right() is not None:
					return self.search_node(parent.get_right(), data)
				else:
					return None

	def delete(self, data):
		results = self.delete_node(self.root, data)
		if results is None:
			print("No such data found to delete:", data)
		else:
			print("delete successful:", data)

	def delete_node(self, parent, data):
		# Case 1: Empty tree
		if parent is None:
			return None

		# Case 2: Root is to be deleted
		elif self.root.get_data() == data:
			# Update root
			if parent.get_right() is not None:
				self.set_root(parent.get_right())
			elif parent.get_left() is not None:	# Set left child as new root if no right children
				self.set_root(parent.get_left())
			else: # Becomes empty tree
				self.set_root(None)
			return parent

		# Case 3: Go left
		elif parent.get_data() > data:
			if parent.get_left() is not None:
				# Left child to be deleted
				if parent.get_left().get_data() == data:
					# Save temp grandchildren
					l_grandchild = parent.get_left().get_left()
					r_grandchild = parent.get_left().get_right()
					# Reset left child
					parent.set_left(None)
					# Re-insert grandchildren from the top
					if l_grandchild is not None:
						self.insert(l_grandchild.get_data())
					if r_grandchild is not None:
						self.insert(r_grandchild.get_data())
					return data
				# Recurse left
				else:
					parent = parent.get_left()
					self.delete_node(parent, data)
			else:
				return None

		# Case 3: Go right
		elif parent.get_data() < data:
			if parent.get_right() is not None:
				# Left child to be deleted
				if parent.get_right().get_data() == data:
					# Save temp grandchildren
					l_grandchild = parent.get_right().get_left()
					r_grandchild = parent.get_right().get_right()
					# Reset left child
					parent.set_right(None)
					# Re-insert grandchildren from the top
					if l_grandchild is not None:
						self.insert(l_grandchild.get_data())
					if r_grandchild is not None:
						self.insert(r_grandchild.get_data())
					return data
				# Recurse left
				else:
					parent = parent.get_right()
					self.delete_node(parent, data)
			else:
				return None

	# Worked fine except I literally forgot to include exception if it's the root
	def delete_node2(self, parent, data):
		# Case 1: Empty tree
		if parent is None:
			return None
		# Case 2: Parent (root) is node to be deleted
		elif parent.get_data() == data:
			# Update root
			self.set_root(parent.get_right())
			print("New root:", self.get_root())
			# Re-insert any left child(ren) of parent
			if parent.get_left() is not None:
				self.insert_node(self.root, parent.get_left())
			return parent
		# Recurse!
		else:
			# Go left
			if parent.get_data() > data:
				if parent.get_left() is None:
					return None
				else:
					return self.delete_node(parent.get_left(), data)
			else:
				if parent.get_right() is None:
					return None
				else:
					return self.delete_node(parent.get_right(), data)

	# First (not working) version, better way of doing it in delete_node()
	def delete_node3(self, parent, data):
		# Case 1: left child is the target node
		if parent.get_left() == data:
			# Check/get/set left grandchild
			if parent.get_left().get_left() is not None:
				l_grandchild = parent.get_left().get_left()
				parent.set_left(l_grandchild)
				return parent.get_left()
			# Check/get/set right grandchild
			if parent.get_right().get_right() is not None:
				r_grandchild = parent.get_left().get_right()
				parent.set_right(r_granchild)
				return parent.get_left()

		# Case 2: right child is target node
		elif parent.get_right() == data:
			# Check/get/set left grandchild
			if parent.get_right().get_left() is not None:
				l_grandchild = parent.get_right().get_left()
				parent.set_left(l_grandchild)
				return parent.get_right()
			# Check/get/set right grandchild
			if parent.get_right().get_right() is not None:
				r_grandchild = parent.get_right().get_right()
				parent.set_right(r_granchild)
				return parent.get_right()

		else:
			# Go left
			if parent.get_left() is not None:
				return self.delete_node(parent.get_left(), data)
			elif parent.get_right() is not None:
				return self.delete_node(parent.get_right(), data)
			else:
				print("Wut. no data found bud")
				return None

	def preorder_traverse(self):
		print("Traversing pre-order...")
		self.pre_traverse(self.root)

	def pre_traverse(self, parent):
		# 1. Print current node
		print(parent.get_data())
		# 2. Recursively print left branch
		if parent.get_left() is not None:
			self.pre_traverse(parent.get_left())
		# 3. Recursively print right branch
		if parent.get_right() is not None:
			self.pre_traverse(parent.get_right())

	def inorder_traverse(self):
		print("Traversing in order...")
		self.in_traverse(self.root)

	def in_traverse(self, parent):
		# 1. Recurse through left branch
		if parent.get_left() is not None:
			self.in_traverse(parent.get_left())
		# 2. Print current node
		print(parent.get_data())
		# 3. Recurse through right branch
		if parent.get_right() is not None:
			self.in_traverse(parent.get_right())

	def postorder_traverse(self):
		print("Traversing post order...")
		self.post_traverse(self.root)

	def post_traverse(self, parent):
		# 1. Recurse through left branch
		if parent.get_left() is not None:
			self.post_traverse(parent.get_left())
		# 2. Recurse through right branch
		if parent.get_right() is not None:
			self.post_traverse(parent.get_right())
		# 3. Print current node
		print(parent.get_data())



def main():
	tree = BST()
	tree.insert(5)
	tree.insert(10)
	tree.insert(2)
	#search_result = tree.search(5)
	#search_result1 = tree.search(4)
	#tree.delete(2)
	#tree.delete(11)
	print("Root:", tree.get_root().get_data())
	tree.preorder_traverse()
	tree.inorder_traverse()
	tree.postorder_traverse()


	# if search_result is not None:
	# 	print(search_result)
	# else:
	# 	print("No such data found.")

	# if search_result1 is not None:
	# 	print(search_result1)
	# else:
	# 	print("No such data found #2.")

if __name__ == '__main__':
	main()