"""
Given a directed graph, design an algorithm to find out whether there is a route between two nodes
"""




def route_between_nodes_using_dfs(graph, start, end):

	visited = set()
	import pdb; pdb.set_trace()
	def dfs(node):
		if node == end:
			return True
		visited.add(node)
		for neigh in graph.get(node, []):
			if neigh not in visited:
				dfs(neigh)

	return dfs(start)



	# def dfs_with_stack(node):
	# 	if node == end:
	# 		return True
	# 	stack = [node]
	# 	visited.add(node)
	# 	while stack:
	# 		s = stack.pop(-1)
	# 		for neigh in graph.get(s, []):
	# 			if neigh == end:
	# 				return True
	# 			if neigh not in visited:
	# 				stack.append(neigh)
	# 				visited.add(neigh)
	# 	return False
	# return dfs_with_stack(start)


def route_between_nodes_using_bfs(graph, start, end):
	if start == end:
		return True
	visited = set()
	queue = []
	queue.append(start)
	while len(queue) > 0:
		u = queue.pop(0)
		visited.add(u)
		for v in graph.get(u, []):
			if v not in visited:
				if v == end:
					return True
				visited.add(v)
				queue.append(v)
	return False





graph = {
	0: [1, 5],
	1: [3],
	2: [1],
	3: [2],
	4: [1, 3]
}
print(route_between_nodes_using_dfs(graph, 0, 3))
# print(route_between_nodes_using_bfs(graph, 0, 3))

# print(route_between_nodes_using_dfs(graph, 0, 5))
# print(route_between_nodes_using_bfs(graph, 0, 5))

# print(route_between_nodes_using_dfs(graph, 1, 5))
# print(route_between_nodes_using_bfs(graph, 1, 5))
