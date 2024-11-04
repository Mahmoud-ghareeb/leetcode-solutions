class Solution:
    def compressedString(self, word: str) -> str:
        mem = ""
        l = 0
        sol = ""

        for i in word:
            if mem == "":
                mem += i
                l += 1
                continue
            
            if i == mem:
                if l < 9:
                    l += 1
                else:
                    sol += "9"+i
                    l = 1
            else:
                sol += str(l)+mem
                mem = i
                l = 1
        sol += str(l)+mem
        return sol
            


        