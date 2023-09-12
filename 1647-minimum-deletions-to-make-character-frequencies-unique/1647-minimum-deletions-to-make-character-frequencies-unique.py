from collections import defaultdict
class Solution:
    def minDeletions(self, s: str) -> int:

        freq = self.freq(s)
        arr = sorted(freq.values(), reverse=True)
        lt = 0
        out = 0
        for i, el in enumerate(arr):
            if i == 0: continue
            a, b = el, arr[lt] 
            if a >= b:
                out += (a-b+1)
                arr[i] -= (a-b+1)
                if arr[i] <= 0:
                    lt -= 1
            lt += 1

        return out

    def freq(self, s):
        d = defaultdict(int)
        for i in s:
            d[i] += 1

        return d

        