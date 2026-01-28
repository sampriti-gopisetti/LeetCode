from collections import deque

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def bfs(sr, sc):
            q = deque([(sr, sc)])
            visited.add((sr, sc))
            area = 1
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        area += 1
            return area

        maxarea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxarea = max(maxarea, bfs(r, c))

        return maxarea
