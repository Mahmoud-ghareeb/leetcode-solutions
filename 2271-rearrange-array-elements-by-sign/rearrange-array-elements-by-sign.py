class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        s_p = []
        s_n = []
        lt = 0
        for i in nums:
            if i >= 0:
                s_p.append(i)
            else:
                s_n.append(i)
        
        sol = []
        l_p, l_n = len(s_p), len(s_n)
        i, j = 0, 0
        while i<l_p or j<l_n:
            if l_p > 0:
                sol.append(s_p[i]) 
                i += 1
            if l_n > 0:
                sol.append(s_n[j])
                j += 1

        return sol
        