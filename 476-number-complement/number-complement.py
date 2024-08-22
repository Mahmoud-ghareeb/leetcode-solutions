class Solution:
    def findComplement(self, num: int) -> int:
        x = bin(num)[2:]
        return num ^ int("1" * len(x), 2)
        