from collections import deque

class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()

        def bfs(sr, sc):
            q = deque([(sr, sc)])
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    visited.add((r, c))
                    bfs(r, c)
                    islands += 1

        return islands
