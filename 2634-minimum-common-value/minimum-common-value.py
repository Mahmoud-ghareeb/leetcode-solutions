class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        d = set(nums1).intersection(set(nums2))

        return sorted(d)[0] if len(d) > 0 else -1
        