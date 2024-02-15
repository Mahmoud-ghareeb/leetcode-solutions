class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        if n<3: return -1
        s = sum(nums)
        print(nums, s)
        for i, num in enumerate(nums):
            print(i, num, s)
            if num < (s-num):
                return s
            if i > (n-3):
                return -1
            
            s -= num

        return -1


        