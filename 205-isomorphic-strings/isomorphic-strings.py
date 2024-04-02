class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        d = defaultdict(str)
        used = set()

        for idx, c in enumerate(s):
            if d[c] == "":
                if t[idx] in used:
                    return False
                d[c] = t[idx]
                used.add(t[idx])
            else:
                if d[c] != t[idx]:
                    return False

        return True

        