class Solution:
    def minimumLength(self, s: str) -> int:
        
        n = len(s)
        p1, p2 = 0, n-1

        while p1 < p2:
            if s[p1] != s[p2]:
                return p2 - p1 + 1

            f_p1, f_p2 = 1, 1
            while True:
                if f_p1: p1 += 1
                if f_p2: p2 -= 1
                if s[p1] != s[p1-1]: f_p1 = 0
                if s[p2] != s[p2+1]: f_p2 = 0
                if f_p1 == 0 and f_p2 == 0: break

                if p2 <= p1: return 0
                    
        return 1 if p1 == p2 else 0




