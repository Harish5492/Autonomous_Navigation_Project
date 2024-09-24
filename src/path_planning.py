import heapq

class Node:
    def __init__(self, x, y, g=0, h=0, f=0, parent=None):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = f
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

def a_star(start, goal, grid):
    open_list = []
    closed_list = set()

    start_node = Node(start[0], start[1], 0, 0)
    goal_node = Node(goal[0], goal[1], 0, 0)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        if (current_node.x, current_node.y) == (goal_node.x, goal_node.y):
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]

        closed_list.add((current_node.x, current_node.y))

        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.x + new_position[0], current_node.y + new_position[1])
            if node_position[0] > len(grid) - 1 or node_position[0] < 0 or node_position[1] > len(grid[0]) - 1 or node_position[1] < 0:
                continue
            if grid[node_position[0]][node_position[1]] != 0:
                continue
            new_node = Node(node_position[0], node_position[1], current_node.g + 1, abs(goal_node.x - node_position[0]) + abs(goal_node.y - node_position[1]))
            new_node.f = new_node.g + new_node.h
            new_node.parent = current_node
            if (new_node.x, new_node.y) in closed_list:
                continue
            heapq.heappush(open_list, new_node)

    return None
