class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        MOD = 10**9 + 7
        memo = {}

        def rec(i, j, remaining_moves):
            if remaining_moves == 0: 
                return 0

            paths = 0
            for di, dj in dirs:
                new_i, new_j = i + di, j + dj

                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                    paths += 1
                else:
                    if (new_i, new_j, remaining_moves - 1) in memo:
                        paths += memo[(new_i, new_j, remaining_moves - 1)]
                    else:
                        memo[(new_i, new_j, remaining_moves - 1)] = rec(new_i, new_j, remaining_moves - 1)
                        paths += memo[(new_i, new_j, remaining_moves - 1)]

            return paths

        return rec(startRow, startColumn, maxMove) % MOD

        