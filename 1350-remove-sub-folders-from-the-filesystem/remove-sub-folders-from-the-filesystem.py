class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        folder = sorted(folder, key=lambda x: len(x))

        sol = []

        for idx,i in enumerate(folder):
            if i == 0:
                continue

            sol.append(i)
            for j in range(idx+1, len(folder)):
                if folder[j] == 0:
                    continue
                    
                if folder[j][:len(i)+1] == i+'/':
                    folder[j] = 0


        return sol


        