class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        m = 0
        n = 0

        for i in stones:
            m = max(m, i[0], i[1])
        
        m += 1
        n = m

        # arr = [[0 for i in range(n)] for j in range(m)]
        d = {}
        for i in stones:
            d[(i[0], i[1])] = 1


        def dfs(i, j, c):
            if i<0 or i>=m or j<0 or j>=n or d.get((i, j), 0) != 1: return 0

            d[(i, j)] += 1

            for k, l in d:
                if l == j and d.get((k, l), 0) == 1:
                    c = dfs(k, l, c + 1)

            for k, l in d:
                if k == i and d.get((k, l), 0) == 1:
                    c = dfs(k, l, c + 1)

            return c

        sol = 0
        # print(d)
        for i, j in d:
            sol += dfs(i, j, 0)

        return sol
        