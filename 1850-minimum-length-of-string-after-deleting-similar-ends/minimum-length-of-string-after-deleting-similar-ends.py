class Solution:
    def minimumLength(self, s: str) -> int:
        
        n = len(s)
        p1, p2 = 0, n-1

        while p1 < p2:
            print(p1, p2)
            if s[p1] != s[p2]:
                return p2 - p1 + 1

            while True:
                p1 += 1
                if s[p1] != s[p1-1]:
                    break
                if p2 <= p1:
                    return 0
            
            while True:
                p2 -= 1
                if s[p2] != s[p2+1]:
                    break
                if p2 <= p1:
                    return 0
        print(p1, p2)
        return 1 if p1 == p2 else 0




