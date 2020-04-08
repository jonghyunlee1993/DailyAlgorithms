graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

# 방문한 노드를 순서대로 찾아가기
def bfs(graph, start_node):
	visit = list()
	queue = list()

	queue.append(start_node)

	while queue:
		node = queue.pop(0)

		if node not in visit:
			visit.append(node)
			queue.extend(graph[node])

	return visit

def dfs(graph, start_node):
	visit = list()
	stack = list()

	stack.append(start_node)

	while stack:
		node = stack.pop(-1)

		if node not in visit:
			visit.append(node)
			stack.extend(graph[node])

	return visit

if __name__ == "__main__":
	print("BFS")
	print(bfs(graph, "A"))

	print()

	print("DFS")
	print(dfs(graph, "A"))
