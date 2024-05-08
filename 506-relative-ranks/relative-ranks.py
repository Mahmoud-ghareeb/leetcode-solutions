class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        idx = defaultdict(int)

        for i in range(len(score)):
            idx[score[i]] = i

        temp = sorted(score, reverse=True)

        d = {
            0: 'Gold Medal',
            1: 'Silver Medal',
            2: 'Bronze Medal'
        }

        for i in range(len(score)):
            if i < 3:
                score[idx[temp[i]]] = d[i]
            else:
                score[idx[temp[i]]] = str(i+1)

        return score
        