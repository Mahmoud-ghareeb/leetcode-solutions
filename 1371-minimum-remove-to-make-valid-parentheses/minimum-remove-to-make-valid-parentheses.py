class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = set()
        to_remove = set()

        for idx, c in enumerate(s):
            if c == '(':
                stack.add(idx)
            elif c == ')':
                try:
                    stack.pop()
                except:
                    to_remove.add(idx)
        all_ = stack | to_remove 
        sol = ""
        for idx,c in enumerate(s):
            if idx not in all_:
                sol += c

        return sol
        