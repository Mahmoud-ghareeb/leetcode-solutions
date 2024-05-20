from itertools import combinations

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        sol = 0
        for i in range(1, len(nums)+1):
            b = 0
            for x in combinations(nums, i):
                l = 0
                for j in x:
                    l ^= j
                b += l
                
            sol += b
            
        return sol

        