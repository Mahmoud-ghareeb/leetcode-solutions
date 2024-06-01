class Solution:
    def scoreOfString(self, s: str) -> int:
        sol = 0
        for i in range(len(s)-1):
            sol += abs(ord(s[i]) - ord(s[i+1]))

        return sol
        