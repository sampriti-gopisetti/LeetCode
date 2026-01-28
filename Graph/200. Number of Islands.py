class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows=len(grid)
        cols=len(grid[0])
        islands=0
        visited=set()

        def bfs(r, c):
            q=collections.deque()
            q.append((r,c))
            directions=[[0,1],[1,0],[0,-1],[-1,0]]
            while q:
                row,col=q.popleft()
                for dr, dc in directions:
                    r=row+dr
                    c=col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visited:
                        visited.add((r,c))
                        q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    visited.add((r,c))
                    bfs(r,c)
                    islands+=1
        
        return islands