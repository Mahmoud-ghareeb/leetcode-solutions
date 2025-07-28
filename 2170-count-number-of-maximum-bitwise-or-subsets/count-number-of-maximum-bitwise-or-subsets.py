class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:


        max_or = 0
        for num in nums:
            print(num)
            max_or |= num

        result = []

        for r in range(1, len(nums) + 1):
            result.extend(combinations(nums, r))
        res = 0
        for i in result:
            tmp = 0
            for j in i:
                tmp |= j
            if tmp == max_or:
                res += 1


        return res
            