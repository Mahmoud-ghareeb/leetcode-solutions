class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        d = Counter(arr)
        d = sorted(d.items(), key=lambda x: x[1])

        sol = len(d)
        for num, c in d:
            if k <= 0: 
                return sol

            if c <= k: 
                k -= c
                sol -= 1
            else:
                return sol
        return sol