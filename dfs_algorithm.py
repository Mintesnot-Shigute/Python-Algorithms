class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Examp
graph = Graph()
graph.add_edge(1, [2, 3])
graph.add_edge(2, [4, 5])
graph.add_edge(3, [])
graph.add_edge(4, [])
graph.add_edge(5, [6, 7])
graph.add_edge(6, [])
graph.add_edge(7, [])

start_node = 1
print("DFS traversal starting from node", start_node)
dfs(graph.graph, start_node)
