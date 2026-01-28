class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows=len(grid)
        cols=len(grid[0])
        maxarea=0
        visited=set()

        def bfs(r,c):
            q=collections.deque()
            q.append((r,c))
            directions=[[0,1],[1,0],[-1,0],[0,-1]]
            area=1
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    r=row+dr
                    c=col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c]==1 and (r,c) not in visited:
                        visited.add((r,c))
                        q.append((r,c))
                        area+=1
            return max(area,maxarea)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    visited.add((r,c))
                    maxarea=bfs(r,c)

        return maxarea