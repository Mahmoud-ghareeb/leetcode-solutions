class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False

        t = round(math.log(n, 2), 10)
        return t-int(t) == 0
        