class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)

        sol = []
        for i in range(1, n+1):
            if i not in nums:
                sol.append(i)

        return sol