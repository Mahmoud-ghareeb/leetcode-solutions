class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = 1
        n = len(nums)
        if n < 3:
            return set(nums)
        nums = sorted(nums)
        l = set()
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                c+=1
                if c > (n//3):
                    l.add(nums[i-1])

            else:
                c = 1

        return l