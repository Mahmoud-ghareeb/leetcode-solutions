class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if k >= len(num):
            return "0"
        
        stack = []
        i = 0

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        stack = stack[:-k] if k > 0 else stack

        sol = ("".join(stack)).lstrip("0")

        return "0" if not sol else sol



                


                    

            

            


