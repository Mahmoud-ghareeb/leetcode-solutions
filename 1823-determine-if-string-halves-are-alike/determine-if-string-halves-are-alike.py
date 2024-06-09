class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b, l = 0, 0, len(s)
        v = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

        for i in range(l//2):
            # print(i, )
            if s[i] in v:
                a += 1
            if s[l-(i+1)] in v:
                b += 1

        return a == b


