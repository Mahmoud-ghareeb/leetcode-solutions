class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        max_n = 0

        for i in nums:
            max_n = max_n | i

        n = len(nums)
        @cache
        def recur(cur_or, i):
            if i == n and cur_or != max_n:
                return 0
            if cur_or == max_n:
                return 2 ** (n-i)
            
            cnt = 0
            cnt += recur(cur_or|nums[i], i+1)
            cnt += recur(cur_or, i+1)
            return cnt

        return recur(0, 0)


        