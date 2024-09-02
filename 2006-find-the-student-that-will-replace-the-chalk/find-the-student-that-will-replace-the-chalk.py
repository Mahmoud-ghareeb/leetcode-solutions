class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        n = k // s
        k -= n * s

        i = 0
        while k > 0:
            if k < chalk[i]: return i

            k -= chalk[i]
            i += 1

        return i