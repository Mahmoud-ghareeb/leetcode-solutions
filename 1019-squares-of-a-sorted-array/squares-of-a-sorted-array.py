class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        numss = sorted(nums, key=lambda x: abs(x))
        return [num**2 for num in numss]
        