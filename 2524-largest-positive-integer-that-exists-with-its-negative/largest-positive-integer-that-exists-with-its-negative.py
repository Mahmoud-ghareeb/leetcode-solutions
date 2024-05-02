class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        d = defaultdict(int)
        for num in nums:
            d[num] = 1

        sol = -1
        for i in nums:
            if d[-1*i] == 1:
                sol = max(sol, abs(i))

        return sol
        