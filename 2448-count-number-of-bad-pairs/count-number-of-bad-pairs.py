class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        n = len(nums)
        hel = [nums[i]-i for i in range(n)]

        count_similar = Counter(hel)
        sol = 0

        def spc_fact(n):
            # if n == 1: return 0
            tmp = 0
            for i in range(n-1, 0, -1):
                tmp += i
            
            return tmp

        for i, j in count_similar.items():
            sol += spc_fact(j)

        return spc_fact(len(nums))-sol
        
