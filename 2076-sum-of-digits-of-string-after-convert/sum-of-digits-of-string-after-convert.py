class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        s = ''.join([str(ord(i) - 96) for i in s])
        
        for _ in range(k):
            temp = 0
            for i in s:
                temp += int(i)

            s = str(temp)

        return int(s)

        