from collections import deque
from time import perf_counter


def bfs(g, n, m, briefcase_position):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Initialize the queue with the starting position and shift
    q = deque([(0, 0, 1)])  # Start from (0, 0) with shift 1
    visited = set()
    visited.add((0, 0))

    # To keep track of the path
    previous = {}
    previous[(0, 0)] = None  # Starting position has no previous cell

    while q:
        x, y, shift = q.popleft()

        # Check if we've reached the briefcase position
        if (x, y) == briefcase_position:
            return shift - 1, previous  # Return the distance and the previous map

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Ensure nx, ny are within bounds and not visited
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                # Check if it's an even or odd shift
                if shift % 2 == 0:  # Even shift - check for walls
                    if g[nx][ny] != -1:  # Not a wall
                        visited.add((nx, ny))
                        q.append((nx, ny, shift + 1))
                        previous[(nx, ny)] = (x, y)  # Track the path
                else:  # Odd shift - can move freely
                    visited.add((nx, ny))
                    q.append((nx, ny, shift + 1))
                    previous[(nx, ny)] = (x, y)  # Track the path

    return -1, None  # If no path found


def print_path(previous, start, end):
    path = []
    while end is not None:
        path.append(end)
        end = previous[end]
    path.reverse()  # Reverse the path to start from the beginning
    return path


if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    g = []
    briefcase_position = None

    for i in range(n):
        row = list(map(int, input().split()))

        # Ensure the row has the expected number of columns
        if len(row) != m:
            print(f"Error: Expected {m} elements in row {i + 1}, but got {len(row)}.")
            exit(1)

        g.append(row)

        # Find the briefcase position
        for j in range(m):
            if row[j] == 2:
                briefcase_position = (i, j)

    # Ensure we found the briefcase position
    if briefcase_position is None:
        print(-1)
    else:
        distance, previous = bfs(g, n, m, briefcase_position)
        print(distance)

        if distance != -1:
            path = print_path(previous, (0, 0), briefcase_position)
            print("Win is:", briefcase_position)
            print("Path to the briefcase:", path)
