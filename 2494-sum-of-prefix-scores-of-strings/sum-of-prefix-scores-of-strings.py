class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        d = defaultdict(int)

        for w in words:
            for i in range(len(w)):
                d[w[:i+1]] += 1

        sol = []

        for w in words:
            tmp = 0
            for i in range(len(w)):
                tmp += d[w[:i+1]]
            sol.append(tmp) 

        return sol               