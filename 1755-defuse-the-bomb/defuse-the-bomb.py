class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        n = len(code)
        if k == 0:
            return [0] * n

        prefix = []
        prev = 0
        for i in code:
            prev += i
            prefix.append(prev)
        

        sol = []
        if k > 0:
            for i in range(n):
                tmp = 0
                for j in range(1, k+1):
                    new_idx = (i+j)%n
                    tmp += code[new_idx]
                sol.append(tmp)
        else:
            k = k*-1
            for i in range(n):
                tmp = 0
                for j in range(1, k+1):
                    new_idx = (i-j)%n
                    tmp += code[new_idx]
                sol.append(tmp)
        
        return sol