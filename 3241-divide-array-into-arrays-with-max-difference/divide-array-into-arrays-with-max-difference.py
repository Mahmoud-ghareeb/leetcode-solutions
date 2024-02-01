class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        sol = []
        for i, num in enumerate(nums):
            if i == 0:
                j, temp = 1, [num]
            elif j >= 3:
                sol.append(temp)
                j = 1
                temp = [num]
            elif num - temp[0] <= k:
                temp.append(num)
                j += 1
            else:
                return []

            # print(temp)
        sol.append(temp)

        return sol

            
            

            


        