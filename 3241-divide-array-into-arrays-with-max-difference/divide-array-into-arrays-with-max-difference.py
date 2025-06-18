class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        if len(nums)%3 != 0:
            return []

        nums.sort()

        results = []

        for i in range(len(nums)//3):
            idx = i*3
            tmp = nums[idx:idx+3]
            if tmp[2] - tmp[0] > k:
                return []

            results.append(tmp)


        return results 

        