import heapq

# Goal state as a 2D list
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Directions for possible moves: up, down, left, right
directions = [(-3, 'up'), (3, 'down'), (-1, 'left'), (1, 'right')]


# Convert a 2D list to a tuple (for easy comparison and use in sets)
def convert_to_tuple(state):
    return tuple([item for sublist in state for item in sublist])


# Convert a tuple back to a 2D list
def convert_to_2d(state_tuple):
    return [list(state_tuple[i:i + 3]) for i in range(0, 9, 3)]


# Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for row in range(3):
        for col in range(3):
            value = state[row][col]
            if value == 0:
                continue
            target_row, target_col = divmod(value - 1, 3)
            distance += abs(row - target_row) + abs(col - target_col)
    return distance


# Get possible valid moves
def get_neighbors(state):
    neighbors = []
    blank_row, blank_col = [(row, col) for row in range(3) for col in range(3) if state[row][col] == 0][0]

    for direction, action in directions:
        new_row, new_col = blank_row + direction // 3, blank_col + direction % 3

        # Check if the move is within bounds
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            # Swap blank space with the number in the new position
            new_state = [row[:] for row in state]  # Make a copy of the state
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], \
            new_state[blank_row][blank_col]
            neighbors.append((new_state, action))

    return neighbors


# A* algorithm to solve the puzzle
def solve_puzzle(start):
    start_tuple = convert_to_tuple(start)
    goal_tuple = convert_to_tuple(goal)

    open_list = []
    closed_list = set()

    # Push the starting state into the priority queue
    heapq.heappush(open_list, (manhattan_distance(start), 0, start_tuple, []))

    while open_list:
        _, g_cost, current_state_tuple, path = heapq.heappop(open_list)

        current_state = convert_to_2d(current_state_tuple)

        if current_state_tuple == goal_tuple:
            return path  # Return the sequence of moves

        if current_state_tuple in closed_list:
            continue

        closed_list.add(current_state_tuple)

        for neighbor, move in get_neighbors(current_state):
            neighbor_tuple = convert_to_tuple(neighbor)
            if neighbor_tuple not in closed_list:
                f_cost = g_cost + 1 + manhattan_distance(neighbor)
                heapq.heappush(open_list, (f_cost, g_cost + 1, neighbor_tuple, path + [move]))

    return None  # No solution found


# Test the solver
start_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 0, 8]
]  # Example starting configuration

print("Solving the 8-Puzzle8 Largura funcional com grafico...")

solution = solve_puzzle(start_state)
if solution:
    print("Solution found!")
    print("Moves to solve the puzzle:", solution)
else:
    print("No solution found.")