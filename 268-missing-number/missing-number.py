class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        s = sum(nums)
        ss = (len(nums)*(len(nums)+1))//2

        return ss-s
        