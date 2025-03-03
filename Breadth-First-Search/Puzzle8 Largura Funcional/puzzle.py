import queue
from collections import deque
import time

initial_state = [
        [1, 2, 3],
        [4, 6, 0],
        [7, 5, 8]
    ]

objective_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]


# Define the PuzzleState object class
class PuzzleState:
    def __init__(self, board, parent=None,move=None, g=1, n=0, exp=0):
        self.board = board
        self.parent = parent  # Store the parent as a reference to the parent state
        self.move = move
        self.g = g  # The generation number or cost to reach this state
        self.n = n  # The depth (level) in the search tree
        self.exp = exp  # Number of expansions (can be used for debugging or analysis)

    def print_state(self):
        print(f'Generation: {self.g} '
              f'Level: {self.n} '
              f'Expansions: {self.exp}')
        for row in self.board:
            print(row)

    def convert_state_to_tuple(self):
        # Convert the board into a tuple of tuples (hashable)
        return tuple(item for row in self.board for item in row)


def is_goal_state(o_state, c_state):
    return o_state == c_state.board


def generate_successors(state):
    blank_pos = None
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                blank_pos = (row, col)
                break
        if blank_pos:
            break

    row, col = blank_pos
    successors = []
    directions = [
        (-1, 0),     # up
        (0, -1),     # left
        (0, 1),      # right
        (1, 0)       # down
    ]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row.copy() for row in state]  # Make a copy of the current state
            new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
            successors.append(new_state)

    return successors


def order_bfs(start_node):
    visited = set()
    queue = deque([start_node])
    generation = 1
    expansions = 0

    while queue:
        current_node = queue.popleft()  # Use popleft to simulate BFS
        expansions += 1

        board_tuple = current_node.convert_state_to_tuple()
        if board_tuple not in visited:
            visited.add(board_tuple)
            result = is_goal_state(objective_state, current_node)

            if result:
                print("Goal found!")
                return current_node

            successors = generate_successors(current_node.board)
            if successors:
                current_node.exp += 1

            for move, item in enumerate(successors, 1):  # Track the move direction
                successor_tuple = convert_to_tuple(item)
                if successor_tuple not in visited:
                    generation += 1
                    child_state = PuzzleState(item, parent=current_node, g=generation, n=current_node.n + 1, exp=expansions)
                    queue.append(child_state)  # Append to the end for BFS

    print("Goal not found")
    return False

def order_dfs(start_node, visited=None):
    if visited is None:
        visited = set()

    # If the current node is the goal state, return it
    if is_goal_state(objective_state, start_node):
        print("Goal found!")
        return start_node

    board_tuple = start_node.convert_state_to_tuple()

    if board_tuple not in visited:
        visited.add(board_tuple)
        successors = generate_successors(start_node.board)

        for move, item in enumerate(successors, 1):
            # Create a new state object for the child node
            child_state = PuzzleState(item, parent=start_node, move=move, g=start_node.g + 1, n=start_node.n + 1, exp=start_node.exp + 1)
            result = order_dfs(child_state, visited)

            if result:
                return result  # If a goal state is found, return it

    return None


def convert_to_tuple(board):
    return tuple(item for row in board for item in row)


# Initialize the puzzle state object
initial_state_obj = PuzzleState(initial_state)
print("Initial State: \n")
initial_state_obj.print_state()
print("\n")

# Record start time
start_time = time.time()

# # Run the BFS and print the result
# result = order_bfs(initial_state_obj)

# Run the DFS and print result
result = order_dfs(initial_state_obj)

# Record end time
end_time = time.time()

if result:
    result.print_state()

# Print the time it took to find the solution
elapsed_time = end_time - start_time
print(f"\nTime taken to find the solution: {elapsed_time:.4f} seconds")