class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1: return 1
        s_n = (n*(n+1))//2
        for i in range(n//2, n):
            s = (i*(i+1))//2
            j = i-1
            s_1 = (j*(j+1))//2
            print(s, s_n)
            if s == s_n-s_1:
                return i

        return -1

        