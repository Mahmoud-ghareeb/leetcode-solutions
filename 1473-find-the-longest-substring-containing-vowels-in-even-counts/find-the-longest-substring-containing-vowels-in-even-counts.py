class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        p = 0
        m = [0] * 26
        m[ord("a") - ord("a")] = 1
        m[ord("e") - ord("a")] = 2
        m[ord("i") - ord("a")] = 4
        m[ord("o") - ord("a")] = 8
        m[ord("u") - ord("a")] = 16
        mp = [-1] * 32
        l = 0
        for i in range(len(s)):
            p ^= m[ord(s[i]) - ord("a")]
            if mp[p] == -1 and p != 0:
                mp[p] = i
            l = max(l, i - mp[p])
        return l