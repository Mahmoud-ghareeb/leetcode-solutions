class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        ops = ['+', '-', '*', '/']

        for i in tokens:
            if i in ops:
                if i == '+':
                    ans[-1] = int(ans[-2]) + int(ans[-1])
                    del ans[-2]
                    continue
                elif i == '*':
                    ans[-1] = int(ans[-2]) * int(ans[-1])
                    del ans[-2]
                    continue
                elif i == '-':
                    ans[-1] = int(ans[-2]) - int(ans[-1])
                    del ans[-2]
                    continue
                elif i == '/':
                    ans[-1] = int(int(ans[-2]) / int(ans[-1]))
                    del ans[-2]
                    continue
            else:
                ans.append(i)

        return int(ans[-1])