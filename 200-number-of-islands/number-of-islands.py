class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            if 0>i or i>=m or 0>j or j>=n or grid[i][j] == "0":
                return

            grid[i][j] = "0"

            for k, l in dirs:
                dfs(i+k, j+l)

        sol = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    sol += 1
                    dfs(i, j)
        
        return sol


        