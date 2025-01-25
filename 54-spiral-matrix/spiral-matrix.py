class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix)
        n = len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        vis = set()
        sol = [matrix[0][0]]

        curr = (0, 0)
        vis.add(curr)
        i = 0
        while len(vis) < m*n:
            while True:
                tmp = curr
                tmp = (curr[0]+dirs[i][0], curr[1]+dirs[i][1])
                if tmp not in vis and 0 <= tmp[0] < m and 0 <= tmp[1] < n:
                    curr = tmp
                    sol.append(matrix[curr[0]][curr[1]])
                    vis.add(curr)
                else:
                    break
            
            i = ((i+1)%4)

        return sol






        
        