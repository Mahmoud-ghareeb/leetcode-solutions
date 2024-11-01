class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)

        if n <= 2:
            return s

        sol = [s[0], s[1]]

        for i in range(2, n):
            if s[i] == sol[-1] and s[i] == sol[-2]:
                continue
            sol.append(s[i])

        return ''.join(sol)
        