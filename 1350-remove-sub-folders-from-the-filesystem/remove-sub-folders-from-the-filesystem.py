class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        class Trie:
            def __init__(self):
                self.children = {}
                self.end = 0

        def insert(root, v):
            folders = v[1:].split('/')
            curr = root

            for f in folders:

                if f not in curr.children:

                    node = Trie()
                    curr.children[f] = node

                curr = curr.children[f]

            curr.end = 1

        root = Trie()
        for i in folder:
            insert(root, i)

        sol = []

        curr = root
        
        def dfs(node, path):
            if node.end == 1:
                sol.append(path)
                return 
            if not node.children:
                return
            
            # print(node.children.keys())
            # print(path)
            for i, node in node.children.items():
                dfs(node, path + '/' + i)

        dfs(curr, '')

        return sol


        