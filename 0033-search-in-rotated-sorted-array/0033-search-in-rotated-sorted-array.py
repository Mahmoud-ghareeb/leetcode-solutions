class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        if n < 4:
            return -1 if target not in nums else nums.index(target)
        lt = 0
        rt = n-1
        idx = -1
        while lt<=rt:
            md = (lt+rt) // 2
            # print(md, rt, lt)
            if md == 0 and nums[md] > nums[md+1]:
                idx = md + 1
                break
            elif md == n-1 and nums[md] < nums[md-1]:
                idx = md
                break
            if nums[md+1] > nums[md] < nums[md-1]:
                idx = md
                break
            elif nums[md] > nums[rt]:
                lt = md + 1
            else:
                rt = md - 1
                
        l = bisect.bisect_left(nums[:idx], target)
        if -1<l<n and nums[l] == target:
            return l
        else:
            r = bisect.bisect_left(nums[idx:], target)
            if -1<r+idx<n and nums[r+idx] == target:
                return r+idx
        return -1