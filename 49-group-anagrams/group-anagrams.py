class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sups = [''.join(sorted(s)) for s in strs]
        sol = []
        vis = set()
        for i, s in enumerate(sups):
            temp = []
            for j in range(i, len(strs)):
                if s == sups[j] and j not in vis:
                    vis.add(strs[j])
                    temp.append(strs[j])
                    vis.add(j)
            if temp != []:
                sol.append(temp)



        return sol
