"""
Given a directed graph, design an algorithm to find out whether there is a route between two nodes
"""




def route_between_nodes(graph, start, end):

	visited = set([start])

	# depth first
	def dfs(node):
		if node == end:
			return True

		for neigh in graph(node, []):
			if neigh not in visited:
				return dfs(neigh)

	return dfs(start) if dfs(start) else False



graph = {
	0: [1, 5],
	1: [3],
	2: [1],
	3: [2],
	4: [1, 3]
}

print(route_between_nodes(graph, 4, 2))
