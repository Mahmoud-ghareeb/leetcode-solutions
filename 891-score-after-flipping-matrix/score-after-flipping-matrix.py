class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])

        def flib_row(i):
            for j in range(m):
                grid[i][j] = int(not(grid[i][j]))

        def flib_col(j):
            for i in range(n):
                grid[i][j] = int(not(grid[i][j]))

        def count_0(j):
            cnt = 0
            for i in range(n):
                if grid[i][j] == 0:
                    cnt += 1
                    
            return cnt

        for i in range(n):
            if grid[i][0] == 0:
                flib_row(i)

        for j in range(m):
            if count_0(j) > n//2:
                flib_col(j)

        sol = 0
        for i in range(n):
            b = "0b"
            for j in range(m):
                b += str(grid[i][j])

            sol += int(b, 2)

        return sol
        