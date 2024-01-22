class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        ctr = 1
        sol = [0, 0]
        flag, h, r = 0, 1, 1
        for i in nums:
            if flag == 2: 
                return sol

            if r and ctr > 1 and i == nums[ctr-2]:
                sol[0] = i
                flag += 1
                r = 0
                ctr -= 1

            elif h and i != ctr:
                sol[1] = ctr
                flag += 1
                h = 0
            
            ctr += 1

        if sol[1] == 0:
            sol[1] = ctr
        return sol


            

        