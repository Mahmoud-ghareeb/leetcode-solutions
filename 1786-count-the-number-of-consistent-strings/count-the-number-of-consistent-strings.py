class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        sol = 0
        s_a = set(allowed)
        for i in words:
            if set(i) - s_a == set():
                sol += 1

        return sol
        