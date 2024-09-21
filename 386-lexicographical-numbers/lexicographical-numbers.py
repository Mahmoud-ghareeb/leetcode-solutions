class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        sol = []
        for i in range(1, n+1):
            sol.append(str(i))

        sol.sort()

        return list(map(int, sol))
        