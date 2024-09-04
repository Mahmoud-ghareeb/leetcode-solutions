class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        curr_loc = (0, 0)
        curr_dir = 0

        obstacles = set((i, j) for i, j in obstacles)

        dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

        max_point = curr_loc

        def get_distance(p):
            i, j = p
            return i**2 + j**2

        for c in commands:
            if c == -1:
                curr_dir = (curr_dir + 1) % 4
                continue
            elif c == -2:
                curr_dir = (curr_dir + 3) % 4
                continue
            
            for _ in range(c):
                temp = (curr_loc[0] + dirs[curr_dir][0],  curr_loc[1] + dirs[curr_dir][1])
                if temp in obstacles: break
                curr_loc = temp
            # print(curr_dir, curr_loc, c, dirs[curr_dir])
            if get_distance(curr_loc) > get_distance(max_point):
                max_point = curr_loc
        # print(curr_dir, curr_loc, c, dirs[curr_dir])
        return max_point[0] ** 2 + max_point[1] ** 2


        