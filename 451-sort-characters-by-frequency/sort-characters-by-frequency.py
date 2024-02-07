class Solution:
    def frequencySort(self, s: str) -> str:
        
        d = defaultdict(int)

        for i in s:
            d[i] += 1

        d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        sol = ""
        for i in d:
            sol += i[0]*i[1]

        return sol