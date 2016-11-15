# Uses a stack to do depth-first search on a graph implemented using an adjacency list.

# Grab start node and dump linked vertices in stack
# While stack is not empty:
#	pop top one off stack
#	if not yet visited, print, add to visited list, and add popped's linked vertices to stack
#	

def DFS(graph):
	visited = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0}
	stack = []
	all_keys = list(graph)
	print(all_keys)
	first_key = all_keys.pop()
	for i in first_key:
		stack.append(i)
	while stack is not None:
		next_node = stack.pop()
		# If next node has not yet been visited
		if visited[next_node] == 0:
			#print(next_node)
			visited[next_node] = 1
			next_node_neighbors = graph[next_node]
			for i in range(len(next_node_neighbors)):
				stack.append(next_node_neighbors[i])

def main():
	graph = {
			'a':('b','c'),
			'b':('d', 'e'),
			'c':('a', 'f'),
			'd':('b',),
			'e':('b', 'f'),
			'f':('c', 'e')
			}
	DFS(graph)

main()