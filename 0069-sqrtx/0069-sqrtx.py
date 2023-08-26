class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        
        lt, rt = 0, x
        
        while lt<=rt:
            md = (lt+rt) // 2
            
            if md*md == x:
                return md
            elif md*md < x:
                lt  = md + 1
                ans = md
            else:
                rt = md - 1
                
        return lt-1
        