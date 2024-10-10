class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        n = len(nums)
        r_max = [None] * n
        r_max[-1] = nums[-1]

        for i in range(n-2, -1, -1):
            r_max[i] = max(r_max[i+1], nums[i])

        # print(r_max)
    
        i = 0
        rgt = 0
        max_s = 0

        while rgt < n:
            while i < rgt and nums[i] > r_max[rgt]:
                i += 1

            max_s = max(max_s, rgt - i)
            rgt += 1

        return max_s
        