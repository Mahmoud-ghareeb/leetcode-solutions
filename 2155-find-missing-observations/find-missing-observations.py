class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        s = sum(rolls)
        candidate = []

        for i in range(1, n+1):
            temp = mean * (m + i) - s
            s += temp
            candidate.append(temp)

        pos, neg = 0, 0
        for i in range(n):
            if candidate[i] > 6:
                pos += candidate[i] - 6
                candidate[i] = 6
            elif candidate[i] < 1:
                neg += (1 + abs(candidate[i]))
                candidate[i] = 1

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
        