def numDistinctIslands(grid):
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    shapes = set()

    def dfs(r, c, r0, c0, shape):
        if r < 0 or r >= m or c < 0 or c >= n:
            return
        if visited[r][c] or grid[r][c] == 0:
            return

        visited[r][c] = True
        shape.append((r - r0, c - c0))  # relative position
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dfs(r + dr, c + dc, r0, c0, shape)

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1 and not visited[r][c]:
                shape = []
                dfs(r, c, r, c, shape)
                print(f"the shape is {shape}")
                shapes.add(tuple(shape))  # convert to tuple for hashing

    return len(shapes)

grid = [
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1]
]

print(numDistinctIslands(grid))  # Output: 3