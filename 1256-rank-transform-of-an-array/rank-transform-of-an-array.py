from sortedcontainers import SortedSet

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = SortedSet()
        idx = []
        for id, i in enumerate(arr):
            s.add(i)
            idx.append(idx)
        sol = []
        for i in arr:
            sol.append(s.index(i)+1)

        return sol
        