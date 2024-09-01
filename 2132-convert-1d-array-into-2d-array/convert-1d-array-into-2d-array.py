class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l = len(original)
        if m * n != l: return []

        sol = []

        for i in range(0, l, n):
            sol.append(original[i:n+i])

        return sol
        