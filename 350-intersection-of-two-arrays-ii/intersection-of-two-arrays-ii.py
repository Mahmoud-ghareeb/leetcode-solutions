class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = Counter(nums1)
        n2 = Counter(nums2)

        e = set(nums1) & set(nums2)

        res = []
        for i in e:
            res.extend(min(n1[i], n2[i]) * [i])
        
        return res