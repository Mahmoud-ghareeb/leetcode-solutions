class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        if m < 3 or n < 3:
            return 0

        def check_magic(i, j):
            d = defaultdict(int)
            base = 0
            for m in range(j, j+3):
                r = grid[i][m]
                if r <1 or r > 9:
                    return False
                base += r
                d[r] += 1

            #check rows
            for k in range(i+1, i+3):
                temp = 0 
                for m in range(j, j+3):
                    r = grid[k][m]
                    if r <1 or r > 9:
                        return False
                    temp += r
                    d[r] += 1

                if temp != base:
                    return False

            #check cols
            for k in range(j, j+3):
                temp = 0
                for m in range(i, i+3):
                    r = grid[m][k]
                    if r <1 or r > 9:
                        return False
                    temp += r
                    d[r] += 1

                if temp != base:
                    return False

            #check_left_diagonal
            temp = 0
            for f in range(3):
                r = grid[i+f][j+f]
                if r <1 or r > 9:
                    return False
                temp += r
                d[r] += 1
                
            if temp != base:
                return False

            #check_right_diagonal
            temp = 0
            for f in range(3):
                r = grid[i+2-f][j+f]
                if r <1 or r > 9:
                    return False
                temp += r
                d[r] += 1

            if temp != base:
                return False

            if len(d) != 9:
                return False

            return True

        count = 0
        for i in range(m-2):
            for j in range(n-2):
                if check_magic(i, j):
                    count += 1

        return count
            

