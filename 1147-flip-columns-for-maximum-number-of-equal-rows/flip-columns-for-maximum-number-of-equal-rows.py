class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:

        d = defaultdict(int)

        for m in matrix:
            d[''.join(map(str, m))] += 1

        def flip(s):
            tmp = ""
            for i in s:
                if i == '1':
                    tmp += '0'
                else:
                    tmp += '1'

            return tmp

        sol = max(d.values(), default=0)
        
        for i in d:
            tmp = flip(i)
            if tmp in d:
                sol = max(sol, d[i] + d[tmp])
            
            if '0' not in i or '1' not in i:
                sol = max(sol, d[i])


        return sol

        