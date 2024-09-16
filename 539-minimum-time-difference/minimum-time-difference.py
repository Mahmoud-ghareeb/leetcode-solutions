class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        sol = float('inf')
        n = len(timePoints)

        for i in range(n):
            tmp = timePoints[i].split(':')
            m = int(tmp[0]) * 60 + int(tmp[1])

            timePoints[i] = m

        t = sorted(timePoints)
        
        for i in range(1, n):
            sol = min(sol, t[i]-t[i-1])

        return min(sol, t[0]+(1440-t[-1]))
        