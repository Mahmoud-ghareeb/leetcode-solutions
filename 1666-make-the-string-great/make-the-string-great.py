class Solution:
    def makeGood(self, s: str) -> str:
        if s == "": return ""

        sol = []
        for i in range(len(s)):
            if sol == []:
                sol.append(s[i])
                continue

            if s[i].lower() == sol[-1].lower() and s[i] != sol[-1]:
                sol.pop()
            else:
                sol.append(s[i])

        
        return ''.join(sol)


        