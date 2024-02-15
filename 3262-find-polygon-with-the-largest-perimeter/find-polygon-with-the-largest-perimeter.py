class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        if n<3: return -1
        s = sum(nums)
        for i, num in enumerate(nums):
            if num < (s-num):
                return s
            if i > (n-3):
                return -1
            
            s -= num

        return -1


        