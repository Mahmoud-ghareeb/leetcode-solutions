class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        sol = []
        n, m = len(grid), len(grid[0])
        
        for i in range(n-2):
            local_a = []
            for j in range(m-2):
                local_m = 0
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        local_m = max(local_m, grid[k][l])

                local_a.append(local_m)

            sol.append(local_a)

        return sol

        
        