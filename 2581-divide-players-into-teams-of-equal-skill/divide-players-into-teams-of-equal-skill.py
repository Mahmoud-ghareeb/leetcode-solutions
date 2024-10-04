class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        s = sum(skill)
        l = len(skill)//2

        if s%l != 0: return -1

        key = s//l
        space = Counter(skill)

        sol = 0
        for i in skill:
            if space[i] <= 0:
                continue

            tmp = (key-i)
            if tmp not in space or (tmp == i and space[tmp] <= 1) or space[tmp] <= 0:
                print(tmp)
                return -1

            space[tmp] -= 1
            space[i] -= 1
            sol += (i * tmp)

        return sol


        