class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        d = defaultdict(int)

        for i in candidates:
            tmp = format(i, '#032b')
            for j in range(len(tmp)):
                if tmp[j] == "1":
                    d[j] += 1
        
        sol = 0
        for i in d:
            sol = max(sol, d[i])

        return sol
