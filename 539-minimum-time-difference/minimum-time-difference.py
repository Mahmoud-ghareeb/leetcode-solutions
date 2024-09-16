class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        sol = float('inf')
        n = len(timePoints)

        for i in range(n):
            tmp = timePoints[i].split(':')
            m = int(tmp[0]) * 60 + int(tmp[1])

            timePoints[i] = m

        t = sorted(timePoints)
        print(t)
        for i in range(1, n):
            sol = min(sol, t[i]-t[i-1])

        return min(sol, t[0]+(1440-t[-1]))

        # for i in range(n):
        #     tmp = timePoints[i].split(':')
        #     m = int(tmp[0]) * 60 + int(tmp[1])
            
        #     for j in range(i+1, n):
        #         tmp1 = timePoints[j].split(':')
        #         m1 = int(tmp1[0]) * 60 + int(tmp1[1])
        #         m1, m2 = min(m, m1), max(m, m1)
        #         print(m, m1, m2)
        #         sol = min(sol, m2-m1, m1+(1440-m2))

        # return sol
        