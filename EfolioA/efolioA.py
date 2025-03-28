import math
from collections import deque

grelha = [
    [1, 1, 1, 1, -1],
    [1, 10, 1, 2, 10],
    [1, -2, 10, 2, 1],
    [10, 10, 1, 1, 1],
    [-1, 1, 1, 2, -2]
]



# grelha2 = [
#     [1,-5,1,10,1,1,1,1,1,1,1],
#     [1,1,10,1,2,1,10,1,1,1,1],
#     [1,10,10,1,1,1,1,10,1,-3,1],
#     [1,2,-1,10,2,2,1,2,10,1,1],
#     [2,1,1,1,10,2,1,1,2,10,1],
#     [1,2,1,1,1,10,-2,1,2,10,1],
#     [2,1,2,10,1,1,10,1,1,10,1],
#     [1,-1,1,10,1,2,1,1,10,2,1],
#     [1,10,10,10,1,2,-1,10,2,2,1],
#     [1,1,1,1,1,2,10,1,1,1,-4],
#     [1,1,-2,2,1,1,1,2,2,2,1]
# ]


def generateGrelha(grelha):
    transformed_grid = []  # To store the new transformed grid

    for row in grelha:
        # Create a new row to hold the transformed values
        transformed_row = []
        for value in row:
            if value == 1:
                transformed_row.append('.')
            elif value == 10:
                transformed_row.append('#')
            elif value == 2:
                transformed_row.append(':')
            else:
                transformed_row.append(str(abs(value)))  # Absolute value for negative numbers

        # Append the transformed row to the grid
        transformed_grid.append("  ".join(transformed_row))

    # Return the transformed grid
    return transformed_grid

def wrapperGrelha(grelha):
    tamanhoGrelha = len(grelha)
    tam = int((tamanhoGrelha * 3) / 2)
    print("*" + "-" * tam + " " + "-" * tam + "*")
    for index, row in enumerate(grelha):
        if index == int(len(grelha) / 2):
            print("  " + row + "  ")
        else:
            print("| " + row + " |")
    print("*" + "-" * tam + " " + "-" * tam + "*")


class Grid:
    def __init__(self, grid_data):
        self.grid = grid_data  # 2D list representation of the grid
        self.rows = len(grid_data)
        self.cols = len(grid_data[0])

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols

    def is_walkable(self, x, y):
        return self.grid[x][y] != 10  # Check if the cell is not an obstacle

    def is_person(self, x, y):
        """Check if the given coordinates contain a person."""
        return self.grid[x][y] == -1 or self.grid[x][y] == -2

    def add_time(self, x, y):
        return abs(self.grid[x][y])

    def get_cost(self, x, y):
        if self.grid[x][y] == 2:
            return 2  # Difficult terrain
        else:
            return 1  # Normal terrain

    def print_cord(self, x, y):
        return self.grid[x][y]

class BFSResult:
    def __init__(self, people_rescued, time_spent, path_taken):
        self.people_rescued = people_rescued
        self.time_spent = time_spent
        self.path_taken = path_taken  # Store the path as a list of moves


def bfs(grid, entry_points, max_time):
    rows = len(grid)
    cols = len(grid[0])

    # Queue will store states in the form: (current positions of rescuers, time_spent, people_rescued)
    queue = deque([(entry_points, 0, 0)])  # Start with all rescuers' positions

    visited = set()  # To track visited states

    # Initialize best result tracker
    best_overall = None

    while queue:
        current_positions, time_spent, people_rescued = queue.popleft()

        # If the current state has exceeded the max time, stop the search
        if time_spent > max_time:
            continue

        # Check if the current state is the best result so far
        if best_overall is None or (people_rescued > best_overall.people_rescued or
                                    (
                                            people_rescued == best_overall.people_rescued and time_spent < best_overall.time_spent)):
            best_overall = BFSResult(people_rescued, time_spent)

        # For each rescuer, try all possible moves
        new_positions = []
        for (x, y) in current_positions:
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] != 10:  # Can't walk through walls (#)
                    # Add to the new positions
                    new_positions.append((new_x, new_y))
                    # Track people rescued (assuming a person is rescued if the cell value is positive)
                    if grid[new_x][new_y] > 0:
                        people_rescued += 1

        # Add new state to the queue if it's a new state
        new_state = tuple(new_positions)
        if new_state not in visited:
            visited.add(new_state)
            queue.append((new_positions, time_spent + 1, people_rescued))

    return best_overall

# grid = Grid(grelha)

# # print(grid.is_valid(0, 4))
# # print(grid.is_walkable(0, 1))
# print(grid.get_cost(4, 4))
# print(grid.print_cord(4, 4))
# print(grid.is_person(4, 4))
# print(grid.add_time(4, 4))

entry_points = [(0, 2), (4, 2), (2, 0), (2, 4)]

# Directions for BFS (Up, Down, Left, Right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

best_overall = None
max_time = 10
nova_grelha = generateGrelha(grelha)
wrapperGrelha(nova_grelha)


# Perform BFS
best_result = bfs(grelha, entry_points, max_time)

# Print the best route's result
# Output the best result
if best_result:
    print(f"Best result: People rescued = {best_result.people_rescued}, Time spent = {best_result.time_spent}")
    print(f"Path taken for each rescuer:")
    for idx, path in enumerate(best_result.path_taken):
        print(f"Rescuer {idx + 1} path: {path}")
else:
    print("No valid rescue path found.")