class Solution:
    def maxDepth(self, s: str) -> int:
        
        curr, m = 0, 0

        for i in s:
            if i == '(':
                curr += 1
            elif i == ')':
                m = max(m, curr)
                curr -= 1

        return m