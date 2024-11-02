class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        d = sentence.split()
        n = len(d)
        
        for i in range(n):
            if i == n-1:
                if d[i][-1] != d[0][0]:
                    return False
            else:
                if d[i][-1] != d[i+1][0]:
                    return False

        return True
