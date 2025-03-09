from typing import NamedTuple, Optional

initial_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

objective_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

generations = 1

class State(NamedTuple):
    board: tuple  # The 9-position tuple
    generation: int
    parent: Optional["State"]  # Reference to the parent state (None for root)
    depth: int
    expansion: int  # Expansion order

def convert_to_tuple(state_2d):
    return tuple(num for row in state_2d for num in row)

def print_board(state):
    print(f'Generation: {state.generation} '
          f'depth: {state.depth} '
          f'Parent: {state.parent} '
          f'Expansion: {state.expansion} '
          )
    for i in range(0, 9, 3):  # Step through the tuple in chunks of 3
        print(state.board[i], state.board[i + 1], state.board[i + 2])

def generate_successors(state, visited):
    global generations
    """Generates successor states by moving the blank tile (0)."""
    blank_pos = None
    state_2d = [list(state.board[i:i + 3]) for i in range(0, 9, 3)]  # Convert tuple back to 3x3

    for row in range(3):
        for col in range(3):
            if state_2d[row][col] == 0:
                blank_pos = (row, col)
                break
        if blank_pos:
            break

    row, col = blank_pos
    successors = []
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # Up, Left, Right, Down

    count_successors = 0
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [r.copy() for r in state_2d]  # Copy the board
            new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
            if convert_to_tuple(new_state) not in visited:
                generations += 1
                successors.insert(0,State(board=convert_to_tuple(new_state),
                                            generation=generations,
                                            parent=state,
                                            depth=state.depth - 1,
                                            expansion=0))  # Expansion order not tracked here
                if successors:
                    print_board(successors[0])

    return successors

# Iterative DFS function
# Iterative DFS function with depth increase
def dfs_iterative(state, goal):
    """Performs an iterative DFS to find the goal state with increasing depth limits."""
    max_depth = 1  # Start with depth 1
    while True:  # Keep searching until we find a solution
        print(f"Searching with depth limit {max_depth}...")
        visited = set()  # Initialize the visited set
        stack = [(state, max_depth)]  # Stack holds tuples of (state, current depth, max_depth)

        while stack:
            current_state, current_depth = stack.pop(0)  # Pop the latest state from the stack

            if current_state.board in visited:
                continue  # Skip already visited states

            visited.add(current_state.board)  # Mark state as visited

            if current_state.board == goal:
                print("Goal reached!")
                return current_state  # Return the solution state

            if current_state.depth > 0:
                print("\n\n\n####### Expansao do Estado ##########")
                print_board(current_state)
                for next_state in generate_successors(current_state, visited):
                    # When adding the successor, we set its depth to the current depth + 1
                    stack.append((next_state, current_depth - 1))

        # If no solution is found, increment depth and restart from initial state
        max_depth += 1
        # Recreate the state with the new increased depth
        state = State(
            board=state.board,  # Keep the current state board
            generation=generations,
            parent=None,  # You may want to reset the parent as well
            depth=max_depth,  # Update the depth of the state
            expansion=0
        )

        # Reset visited set to start fresh at the new depth level
        visited = set()

    return None

# Example Usage
initial_state = State(
    board=convert_to_tuple(initial_state),
    generation=generations,
    parent=None,
    depth=1,
    expansion=0
)

goal_objective = convert_to_tuple(objective_state)

# print_board(initial_state)
solution = dfs_iterative(initial_state, goal_objective)

if solution:
    print("Solution found!")
else:
    print("No solution exists within the depth limit.")
