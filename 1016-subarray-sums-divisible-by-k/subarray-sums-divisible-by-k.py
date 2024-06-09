class Solution(object):
    def subarraysDivByK(self, nums, k):
        sums = [0] * k
        sums[0] += 1
        
        cnt = 0
        currSum = 0
        
        for i in range(len(nums)):
            currSum = (currSum + nums[i] % k + k) % k
            cnt += sums[currSum] 
            sums[currSum] += 1
        
        return cnt