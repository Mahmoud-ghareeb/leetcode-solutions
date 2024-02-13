class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        def is_pl(s):
            n = len(s)
            for i in range(n//2):
                if s[i] != s[n-i-1]:
                    return False
            return True

        for i in words:
            if is_pl(i):
                return i
        return ""