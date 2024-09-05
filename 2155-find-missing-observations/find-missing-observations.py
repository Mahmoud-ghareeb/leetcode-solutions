class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        s = sum(rolls)
        candidate = []

        pos, neg = 0, 0
        for i in range(1, n+1):
            temp = mean * (m + i) - s
            s += temp
            if temp > 6:
                pos += temp - 6
                temp = 6
            elif temp < 1:
                neg += (1 + abs(temp))
                temp = 1
            candidate.append(temp)

        pos -= neg
        
        for i in range(n):
            if pos == 0: return candidate

            if pos < 0:
                if candidate[i] > 0:
                    temp = min(abs(candidate[i] - 1), abs(pos))
                    candidate[i] -= temp
                    pos += temp

            else:
                if candidate[i] < 6:
                    temp = min(6 - candidate[i], pos)
                    candidate[i] += temp
                    pos -= temp

        return [] if pos else candidate
        