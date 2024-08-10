class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:

        n = len(grid)
        G_M = 3 

        graph = [[0 for _ in range(n*G_M)] for _ in range(n*G_M)]
        idx = {
            '\\': [(0, 0), (1, 1), (2, 2)],
            '/': [(0, 2), (1, 1), (2, 0)]
        }

        #building the graph
        i = 0
        while i < n:
            j = 0
            while j < n:
                if grid[i][j] == "/":
                    for k in idx['/']:
                        graph[i*G_M+k[0]][j*G_M+k[1]] = 1
                elif grid[i][j] == " ":
                    j += 1
                    continue
                else:
                    for k in idx['\\']:
                        graph[i*G_M+k[0]][j*G_M+k[1]] = 1

                j += 1
            i += 1

        #count number of islands ( AKA Regions :) )
        def dfs(i, j):
            if i<0 or i>=G_M*n or j<0 or j>=G_M*n:
                return 0
            # print(i, j)
            if graph[i][j] == 1:
                return 0

            graph[i][j] = 1

            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

        sol = 0
        for i in range(G_M*n):
            for j in range(G_M*n):
                if graph[i][j] == 0:
                    dfs(i, j)
                    sol += 1

        return sol
            

            

        return 0
        