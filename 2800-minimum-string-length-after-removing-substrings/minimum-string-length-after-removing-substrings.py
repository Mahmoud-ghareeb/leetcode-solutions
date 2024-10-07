class Solution:
    def minLength(self, s: str) -> int:

        t = ['AB', 'CD']
        while True:
            l = len(s)
            for i in t:
                idx = s.find(i)
                if idx != -1:
                    s = s[:idx] + s[idx+2:]
                
            if l == len(s):
                return l

        return len(s)

        