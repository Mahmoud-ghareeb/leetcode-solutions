class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        cnt = 0
        n = len(nums)
        for i in range(n-2):
            if nums[i] + nums[i+2] == nums[i+1]/2:
                cnt += 1

        return cnt