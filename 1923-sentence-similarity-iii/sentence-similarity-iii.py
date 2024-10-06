class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1, s2 = sentence1.split(), sentence2.split()
        while s1 and s2 and s1[-1] == s2[-1]:
            s1.pop(), s2.pop()

        return s1[:len(s2)] == s2[:len(s1)]