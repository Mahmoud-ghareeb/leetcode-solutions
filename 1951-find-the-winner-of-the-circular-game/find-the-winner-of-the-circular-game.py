class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        l = [i for i in range(1, n+1)]
        start = 0

        while n > 1:
            cadidate = (k+start)%n
            del l[cadidate-1]
            start = (cadidate-1)%n
            n -= 1

        return l[0]

        