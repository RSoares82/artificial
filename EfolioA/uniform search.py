import heapq


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    # To compare nodes based on path cost for the priority queue
    def __lt__(self, other):
        return self.path_cost < other.path_cost


class Problem:
    def __init__(self, initial_state, goal_state, grid, cost_fn):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.grid = grid  # Grid with different costs for each coordinate
        self.cost_fn = cost_fn  # A function to get the cost of an action

    def is_goal(self, state):
        return state == self.goal_state

    def expand(self, node):
        # Expand a node to generate child nodes by moving in the grid
        children = []
        possible_actions = [
            (-1, 0),  # Up
            (1, 0),  # Down
            (0, -1),  # Left
            (0, 1)  # Right
        ]

        for action in possible_actions:
            next_state = (node.state[0] + action[0], node.state[1] + action[1])
            # Check if the next state is within grid bounds
            if 0 <= next_state[0] < len(self.grid) and 0 <= next_state[1] < len(self.grid[0]):
                cost = self.cost_fn(node.state, next_state)
                child_node = Node(state=next_state, parent=node, action=action, path_cost=node.path_cost + cost)
                children.append(child_node)
        return children

    def result(self, state, action):
        # Return the result of applying an action to the state (for grid, it just adds the action)
        return (state[0] + action[0], state[1] + action[1])


def uniform_cost_search(problem):
    # Create initial node
    initial_node = Node(state=problem.initial_state, path_cost=0)

    # Priority Queue (Min-Heap)
    frontier = []
    heapq.heappush(frontier, initial_node)

    # Set of reached states to avoid revisiting
    reached = set()
    reached.add(problem.initial_state)

    while frontier:
        # Pop the node with the least cost
        node = heapq.heappop(frontier)

        # If it's a goal node, return it
        if problem.is_goal(node.state):
            return node

        # Expand the node and add children to the frontier
        for child in problem.expand(node):
            if child.state not in reached:
                reached.add(child.state)
                heapq.heappush(frontier, child)

    return None  # If no solution is found


def cost_fn(state, next_state):
    # Get the cost of the cell at the next state from the grid
    return grid[next_state[0]][next_state[1]]


def print_grid_with_path(grid, path):
    # Create a grid for printing with the path
    grid_copy = [row[:] for row in grid]  # Make a copy of the grid

    for (x, y) in path:
        grid_copy[x][y] = 'X'  # Mark the path with 'X'

    for row in grid_copy:
        print(' '.join(str(cell) for cell in row))


# Example grid with some cells having a cost of 2
grid = [
    [1, 1, 1, 1, 1],
    [1, 2, 1, 2, 1],
    [1, 1, 1, 1, 1],
    [2, 2, 1, 2, 2],
    [1, 1, 1, 1, 1]
]

# Define initial state and goal state
initial_state = (2, 0)  # Starting point (row 2, column 0)
goal_state = (0, 3)  # Goal point (row 3, column 0)

# Create a problem instance
problem = Problem(initial_state, goal_state, grid, cost_fn)

# Run the Uniform-Cost Search
result_node = uniform_cost_search(problem)

# Print the result path
if result_node:
    path = []
    while result_node:
        path.append(result_node.state)
        result_node = result_node.parent
    path = path[::-1]  # Reverse the path to show from start to goal

    # Print the grid with the path marked
    print("Solution path:")
    print_grid_with_path(grid, path)
else:
    print("No solution found")
