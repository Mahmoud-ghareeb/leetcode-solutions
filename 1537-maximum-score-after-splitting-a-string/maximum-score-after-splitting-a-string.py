class Solution:
    def maxScore(self, s: str) -> int:

        s_1 = sum(map(int, s))
        s_0 = 0
        max_sum = 0

        for i in range(len(s)-1):
            if s[i] == "0":
                s_0 += 1
            else:
                s_1 -= 1
            
            max_sum = max(max_sum, s_0+s_1)

        return max_sum
        