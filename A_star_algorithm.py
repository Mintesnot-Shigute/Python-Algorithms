import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  
        self.h = 0  
        self.f = 0  

    def __lt__(self, other):
        return self.f < other.f

def astar(maze, start, end):
    def heuristic(node, goal):
        return abs(node.position[0] - goal[0]) + abs(node.position[1] - goal[1])

    def get_neighbors(current_node):
        neighbors = []
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_position = (current_node.position[0] + move[0], current_node.position[1] + move[1])
            if 0 <= new_position[0] < len(maze) and 0 <= new_position[1] < len(maze[0]) and maze[new_position[0]][new_position[1]] == 0:
                neighbors.append(Node(new_position, current_node))
        return neighbors

    start_node = Node(start)
    goal_node = Node(end)

    open_set = [start_node]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)
        closed_set.add(current_node.position)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Reverse the path to start fr
        neighbors = get_neighbors(current_node)
        for neighbor in neighbors:
            if neighbor.position in closed_set:
                continue

            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor, goal_node.position)
            neighbor.f = neighbor.g + neighbor.h

            if neighbor not in open_set:
                heapq.heappush(open_set, neighbor)

    return None  # no path found 

#Example
maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

start_position = (0, 0)
end_position = (4, 4)

result = astar(maze, start_position, end_position)

if result:
    print("Path found:", result)
else:
    print("No path found.")
