class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        sol = []
        al = Counter(s2.split()) + Counter(s1.split())

        sol = []

        for i in al:
            if al[i] == 1:
                sol.append(i)
        


        return sol