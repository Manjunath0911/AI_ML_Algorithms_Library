# ************* AI Algorithms ****************

# day 1 A* algorithm
import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position  # (x, y)
        self.parent = parent
        self.g = 0  # Distance from start node
        self.h = 0  # Heuristic distance to goal
        self.f = 0  # Total cost

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end):
    open_list = []
    closed_set = set()
    
    start_node = Node(start)
    end_node = Node(end)
    
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)

        if current_node.position == end_node.position:
            # Reconstruct path
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        neighbors = get_neighbors(current_node.position, grid)

        for neighbor_pos in neighbors:
            if neighbor_pos in closed_set:
                continue

            neighbor_node = Node(neighbor_pos, current_node)
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_node.position, end_node.position)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            # Check if this path to neighbor is better
            if not any(neighbor.position == neighbor_node.position and neighbor.f <= neighbor_node.f for neighbor in open_list):
                heapq.heappush(open_list, neighbor_node)

    return None  # No path found

def get_neighbors(position, grid):
    neighbors = []
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dx, dy in directions:
        x, y = position[0] + dx, position[1] + dy
        if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0:  # 0 = walkable
            neighbors.append((x, y))

    return neighbors

# Example grid
# 0 = walkable, 1 = obstacle
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

path = astar(grid, start, end)

print("Path found:" if path else "No path found.")
print(path)
