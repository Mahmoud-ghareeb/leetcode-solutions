class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        d = defaultdict(list)
        for i in range(len(edges)):
            d[edges[i][0]].append(edges[i][1])
        # print(d)
        sol = [[] for i in range(n)]
        # vis = set()
        def dfs(node, curr):
            # if node in vis:
            #     return

            # vis.add(node)    
            
            for i in d[curr]:
                if (
                    not sol[i]
                    or sol[i][-1] != node
                ):
                    sol[i].append(node)
                    dfs(node, i)


        for i in range(n):
            dfs(i, i)


        return sol
        