from itertools import combinations


# Function to check if all villages are covered by a set of guards
def is_covered(grid, guards, n, m):
    # Create a visited grid to mark covered villages
    covered = [[False for _ in range(m)] for _ in range(n)]

    # For each guard, mark the covered villages
    for guard in guards:
        x, y = guard
        # Mark the guard's position itself
        covered[x][y] = True

        # Mark adjacent cells (up, down, left, right)
        if x > 0:
            covered[x - 1][y] = True
        if x < n - 1:
            covered[x + 1][y] = True
        if y > 0:
            covered[x][y - 1] = True
        if y < m - 1:
            covered[x][y + 1] = True

    # Now check if all villages are covered
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not covered[i][j]:
                return False
    return True


# Function to find the smallest dominating set using brute force
def dominating_set(grid, n, m):
    # List all possible positions where guards can be placed
    positions = [(i, j) for i in range(n) for j in range(m) if grid[i][j] != 0]

    # Try all possible combinations of guards (subsets of positions)
    for num_guards in range(1, len(positions) + 1):
        for guard_set in combinations(positions, num_guards):
            if is_covered(grid, guard_set, n, m):
                return guard_set
    return None


# Example grid (1 represents a village, 0 represents an empty space)
grid = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1]
]

n = len(grid)
m = len(grid[0])

# Find the smallest dominating set of guards
result = dominating_set(grid, n, m)

if result:
    print("A possible solution is to place guards at:", result)
else:
    print("No solution found.")
