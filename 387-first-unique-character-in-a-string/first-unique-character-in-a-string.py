class Solution:
    def firstUniqChar(self, s: str) -> int:

        def freq(s):
            d = defaultdict(int)
            for i in s:
                d[i] += 1

            return d

        d = freq(s)

        idx = 0
        for i in s:
            if d[i] == 1:
                return idx
            idx += 1

        return -1

        