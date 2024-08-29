class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        d = {}
        for i in stones:
            d[(i[0], i[1])] = 1


        def dfs(i, j, c):
            if d.get((i, j), 0) != 1: return 0

            d[(i, j)] += 1

            for k, l in d:
                if l == j and d.get((k, l), 0) == 1:
                    c = dfs(k, l, c + 1)

            for k, l in d:
                if k == i and d.get((k, l), 0) == 1:
                    c = dfs(k, l, c + 1)

            return c

        sol = 0
        for i, j in d:
            sol += dfs(i, j, 0)

        return sol
        