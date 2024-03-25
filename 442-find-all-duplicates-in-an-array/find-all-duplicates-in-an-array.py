class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        sol = []
        for i in range(len(nums)):
            if type(nums[i]) == int:
                temp = nums[nums[i]-1]
                if type(temp) == int:
                    nums[nums[i]-1] = (temp, 1) 
                else:
                    sol.append(nums[i])
            else:
                temp = nums[nums[i][0]-1]
                if type(temp) == int:
                    nums[nums[i][0]-1] = (temp, 1) 
                else:
                    sol.append(nums[i][0])

        return sol

        