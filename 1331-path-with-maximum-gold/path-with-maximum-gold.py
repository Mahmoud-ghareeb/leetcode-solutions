class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(i, j, n, m, arr):
            if i<0 or i>=n or j<0 or j>=m or arr[i][j] == 0: return 0

            temp = arr[i][j]
            arr[i][j] = 0
            c = max(temp + dfs(i+k, j+l, n, m, arr) for k,l in dirs)
            arr[i][j] = temp

            return c


        n, m = len(grid), len(grid[0])
        sol = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    sol = max(sol, dfs(i, j, n, m, grid))

        return sol
        