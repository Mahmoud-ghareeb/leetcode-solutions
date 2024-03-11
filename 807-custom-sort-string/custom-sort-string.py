class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        d = defaultdict(int)
        for i in s:
            d[i] += 1

        sol = ""
        for i in order:
            if i in d:
                sol += (i) * d[i]
                d.pop(i)
        
        for i in d:
            sol += (i) * d[i]

        return sol
    
        