class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        sol = []
        

        for i in range(n-k+1):
            flag = 0
            for j in range(i+1, k+i):
                if (nums[j] <= nums[j-1]) or (nums[j] - nums[j-1] != 1):
                    sol.append(-1)
                    flag = 1
                    break
            if flag: continue
            
            sol.append(nums[i + k - 1])

        return sol



            


        