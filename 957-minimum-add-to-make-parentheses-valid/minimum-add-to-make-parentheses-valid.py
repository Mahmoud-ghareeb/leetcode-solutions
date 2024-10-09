class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []
        d = {')' : '(', '}' : '{'}

        for i in s:
            if stack and i in d and stack[-1] == d[i]:
                stack.pop()
            else:
                stack.append(i)
        return len(stack)

        