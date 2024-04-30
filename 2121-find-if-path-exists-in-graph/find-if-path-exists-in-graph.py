class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        d = defaultdict(list)

        for i, j in edges:
            d[i].append(j)
            d[j].append(i)

        vis = set()
        def dfs(node):
            if node == destination: self.sol = True
            if not d[node] or node in vis: return

            vis.add(node)

            for i in d[node]:
                dfs(i)
        
        self.sol = False
        dfs(source)
        return self.sol