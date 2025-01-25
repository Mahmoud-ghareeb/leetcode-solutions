class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)

        for k, v in enumerate(nums):
            d[v].append(k)

        for i in d:
            tmp = target - i
            if tmp in d:
                if i == tmp:
                    if len(d[tmp])>1:
                        return [d[i][0], d[tmp][-1]]
                else:
                    return [d[i][0], d[tmp][-1]]
