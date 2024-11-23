class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:

        d = defaultdict(int)
        def flip(s):
            tmp = ""
            for i in s:
                if i == '1':
                    tmp += '0'
                else:
                    tmp += '1'

            return tmp

        for m in matrix:
            tmp = ''.join(map(str, m))
            d[tmp] += 1
            d[flip(tmp)] += 1

        sol = max(d.values(), default=0)

        return sol

        