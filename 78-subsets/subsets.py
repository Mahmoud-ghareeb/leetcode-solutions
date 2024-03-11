class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        sol = []

        def rec(subset, index):
            sol.append(subset[:]) 
            for i in range(index, len(nums)):
                subset.append(nums[i]) 
                rec(subset, i + 1) 
                subset.pop() 

        rec([], 0)  
        return sol

            
        