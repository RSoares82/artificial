from collections import deque

# 5x5 grid example
grid = [
    ['#', '#', '.', '#', '#'],
    ['#', '.', '.', '#', '#'],
    ['.', '.', '#', '#', '#'],
    ['#', '.', '.', '.', '#'],
    ['#', '#', '#', '.', '1']
]

# Direction vectors for moving up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# BFS function to find the shortest path
def bfs(start, grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [])])  # (current position, path taken)
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        # If we reach the destination
        if grid[x][y] == '1':
            return path + [(x, y)]

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check bounds and if the cell is not a wall
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] != '#':
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(x, y)]))

    return None  # No path found


# Function to print the path on the grid
def print_path(grid, path):
    # Create a copy of the grid to mark the path
    grid_copy = [row[:] for row in grid]

    # Mark the path with 'X' (excluding the starting point)
    for (x, y) in path:
        if grid_copy[x][y] != '1':  # Avoid overwriting the destination
            grid_copy[x][y] = 'X'

    # Print the grid with the path
    for row in grid_copy:
        print(" ".join(row))


# Set starting point
start = (0, 2)

# Run BFS to get the shortest path
path = bfs(start, grid)

if path:
    print("Path found:")
    print_path(grid, path)
else:
    print("No path found")