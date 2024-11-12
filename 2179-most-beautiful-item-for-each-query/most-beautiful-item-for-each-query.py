class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = sorted(items)
        to_search = [item[0] for item in items]
        to_select = []
        
        cand = -1
        for i in items:
            cand = max(cand, i[1])
            to_select.append(cand)

        sol = []

        for i in queries:
            idx = bisect.bisect_right(to_search, i)
            if idx == 0:
                sol.append(0)
            else:
                sol.append(to_select[idx-1])

        return sol