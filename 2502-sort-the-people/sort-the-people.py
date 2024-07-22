class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        ids = {h: idx for idx, h in enumerate(heights)}

        heights = sorted(heights, reverse=True)
        # print(heights)
        # print(ids)
        sol = []

        for h in heights:
            sol.append(names[ids[h]])

        return sol
        