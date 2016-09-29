# Implements a FILO linked list using nodes

class Node:
	def __init__(self, data):
		self.data = data
		self.nexta = None

	def set_next(self, node):
		self.nexta = node
		return

	def get_next(self):
		return self.nexta

	def get_data(self):
		return self.data

class LinkedList:
	def __init__(self):
		self.front = None
		self.back = None
		self.next_item = None

	def set_front(self, item_node):
		self.front = item_node
		return

	def set_back(self, item_node):
		self.back = item_node
		return

	def get_front(self):
		return self.front

	def get_back(self):
		return self.back

	# Adds node to back of line
	# Return item if add was a success.
	def add(self, item):
		node_item = Node(item)
		# If list is empty, add as front and back
		if self.get_front() is None and self.get_back() is None:
			self.set_front(node_item)
			self.set_back(node_item)
			return item
		# Else add item to the back
		else:
			self.get_back().set_next(node_item)
			self.set_back(node_item)

	# Grabs node at front of line
	def remove(self):
		front_node = self.get_front()
		self.set_front(front_node.get_next())
		return front_node

	def print_list(self):
		current = self.get_front()
		while current is not None:
			print(current.get_data())
			current = current.get_next()
		return

def main():
	# Test cases
	linked_list = LinkedList()
	linked_list.add(50)
	linked_list.add(40)
	linked_list.add(60)
	linked_list.add(30)
	linked_list.add(45)
	linked_list.add(55)
	linked_list.add(70)
	linked_list.add(20)
	linked_list.add(35)
	linked_list.add(41)
	linked_list.add(53)
	linked_list.add(54)
	linked_list.add(58)
	linked_list.add(59)
	linked_list.add(80)
	linked_list.print_list()

	linked_list.remove()
	print("\n")
	linked_list.print_list()

if __name__ == '__main__':
	main()