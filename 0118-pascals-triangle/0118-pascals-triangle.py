class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        sol = []
        for i in range(numRows):
            if i == 0: sol.append([1])
            elif i == 1: sol.append([1, 1])
            else:
                temp = [1]
                for j,el in enumerate(sol[-1]):
                    if j == 0: continue
                    temp.append(el+sol[-1][j-1])
                temp.append(1)
                sol.append(temp)

        return sol

                

        