from typing import NamedTuple, Optional
SIZE = 4

# Define the initial state as an empty board (5x5)
initial_state = [None] * SIZE  # Start with an empty board for N=5

generations = 1


class State(NamedTuple):
    board: tuple  # The 5-position tuple representing the board
    generation: int
    parent: Optional["State"]  # Reference to the parent state (None for root)
    depth: int
    expansion: int  # Expansion order


def print_board(state):
    """Print the board representation from the tuple."""
    print(f'Generation: {state.generation} '
          f'Depth: {state.depth} '
          f'Parent: {state.parent} '
          f'Expansion: {state.expansion} '
          )
    board = [['.' for _ in range(SIZE)] for _ in range(SIZE)]
    for row in range(SIZE):
        if state.board[row] is not None:  # If a queen is placed
            board[row][state.board[row]] = 'Q'
    for row in board:
        print(" ".join(row))
    print()


def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def generate_successors(state, visited):
    """Generates successor states by placing a queen on the next row."""
    global generations
    successors = []
    current_row = state.depth

    if current_row == SIZE:
        return successors  # Reached the last row, no more successors to generate

    for col in range(SIZE):
        if is_safe(state.board, current_row, col):
            new_board = list(state.board)
            new_board[current_row] = col
            new_board_tuple = tuple(new_board)

            if new_board_tuple not in visited:
                generations += 1
                new_state = State(board=new_board_tuple,
                                  generation=generations,
                                  parent=state,
                                  depth=current_row + 1,
                                  expansion=generations)  # This could be expansion order
                #successors.append(new_state)
                successors.insert(0, new_state)
                print(f"Generated successor at depth {current_row + 1}:")
                print_board(new_state)
    return successors


# Recursive DFS function
def dfs_recursive(state, goal=None, visited=None, max_depth=0):
    """Performs a recursive DFS to solve the N-Queens problem."""
    if visited is None:
        visited = set()  # Initialize the visited set

    if state.board in visited:
        return None  # Skip already visited states

    visited.add(state.board)  # Mark state as visited

    # If all queens are placed (i.e., we've filled the board with valid queens)
    if state.depth == SIZE:
        print("Solution found!")
        print_board(state)
        return state  # Return the solution state

    if state.depth <= max_depth:
        print("\n\n####### Expansao do Estado ##########")
        print_board(state)
        for next_state in generate_successors(state, visited):
            result = dfs_recursive(next_state, goal, visited, max_depth)
            if result:  # If a solution is found, return it
                return result
    else:
        return None

    return None  # If no solution found, return None


# Example Usage
initial_state = State(
    board=tuple([None] * SIZE),  # Empty board (None means no queen placed)
    generation=generations,
    parent=None,
    depth=0,
    expansion=0
)

# Solve the N-Queens problem for a 5x5 board using DFS
solution = dfs_recursive(initial_state, max_depth=5)

if solution:
    print("Solution found!")
else:
    print("No solution exists within the depth limit.")
