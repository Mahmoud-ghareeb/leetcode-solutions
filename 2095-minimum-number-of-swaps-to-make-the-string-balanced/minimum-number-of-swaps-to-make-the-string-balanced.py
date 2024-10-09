class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        d = {']' : '['}

        for i in s:
            if stack and i in d:
                stack.pop()
            else:
                stack.append(i)
        return (len(stack)+1)//2

        
        