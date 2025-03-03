from typing import NamedTuple, Optional

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
                count_successors += 1
                successors.insert(0,State(board=convert_to_tuple(new_state),
                                            generation=state.generation + count_successors,
                                            parent=state,
                                            depth=state.depth - 1,
                                            expansion=0))  # Expansion order not tracked here
                if successors:
                    print_board(successors[0])

    return successors

# Recursive DFS function
def dfs_recursive(state, goal, visited=None, max_depth=0):
    """Performs a recursive DFS to find the goal state with a depth limit."""
    if visited is None:
        visited = set()  # Initialize the visited set

    if state.board in visited:
        return None  # Skip already visited states

    # Check depth limit
    if state.depth < max_depth:
        return None  # Stop if the depth limit is reached

    visited.add(state.board)  # Mark state as visited
    print("\n\n\n####### Expansao do Estado ##########")
    print_board(state)  # Display current state

    if state.board == goal:
        print("Goal reached!")
        return state  # Return the solution state

    for next_state in generate_successors(state, visited):
        result = dfs_recursive(next_state, goal, visited, max_depth)
        if result:  # If a solution is found, return it
            return result

    return None  # If no solution found, return None

# Example Usage
initial_state = State(
    board=convert_to_tuple(initial_state),
    generation=1,
    parent=None,
    depth=3,
    expansion=0
)

goal_objective = convert_to_tuple(objective_state)

# print_board(initial_state)
solution = dfs_recursive(initial_state, goal_objective, max_depth=0)

if solution:
    print("Solution found!")
else:
    print("No solution exists within the depth limit.")
