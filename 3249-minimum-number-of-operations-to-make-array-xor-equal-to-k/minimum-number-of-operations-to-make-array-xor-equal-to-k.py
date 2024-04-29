class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        sol = nums[0]
        for i in range(1, len(nums)):
            sol ^= nums[i]

        sol ^= k

        return bin(sol).count('1')
        