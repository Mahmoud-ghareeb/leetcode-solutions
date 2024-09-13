class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        
        s = arr[0]
        xors = []
        xors.append(s)
        for i in range(1, len(arr)):
            xors.append(xors[i-1] ^ arr[i])

        sol = []
        for i, j in queries:
            if i == 0:
                sol.append(xors[j])
            else:
                sol.append(xors[j] ^ xors[i-1])

        return sol

        