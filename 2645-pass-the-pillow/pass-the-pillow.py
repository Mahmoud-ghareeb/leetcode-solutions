class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        s = n + (n-2)
        time = (time%s)
        
        if time >= n:
            return n-(time-n)-1

        return time+1
        