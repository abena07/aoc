from collections import deque

def laboratories(input_path):
    with open(input_path) as file:
        items = file.read().split()
        grid = [list(item) for item in items]

    nrows = len(grid)
    ncols = len(grid[0])
    q = deque()
    visited = set()
    count = 0

    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] == 'S':
                start_row, start_col = r, c

    # go down S until hitting a splitter
    r, c = start_row + 1, start_col
    while r < nrows and grid[r][c] == '.':
        r += 1
    if r < nrows and grid[r][c] == '^':
        q.append((r, c))


    while q:
        r, c = q.popleft()

        if (r, c) not in visited and grid[r][c] == '^':
            visited.add((r, c))
            count += 1  

        if grid[r][c] == '^':
            dirs = [
                [1, -1],
                [1, 1]
            ]

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < nrows and 0 <= nc < ncols:
                    # go down diagonally until hitting next splitter
                    rr = nr
                    while rr < nrows and grid[rr][nc] == '.':
                        rr += 1
                    if rr < nrows and grid[rr][nc] == '^' and (rr, nc) not in visited:
                        q.append((rr, nc))

    return count


print(laboratories("../sample.txt"))
