class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # if n == time: return n-1
        s = n + (n-2)
        time = (time%s)
        # print(time)
        if time >= n:
            return n-(time-n)-1

        return time+1
        