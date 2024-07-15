# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        def preprocessing():
            d = defaultdict(list)
            root = descriptions[0][0]
            a = set()
            b = set()
            for i in descriptions:
                d[i[0]].append((i[1], i[2]))
                a.add(i[0])
                b.add(i[1])

            root = a - b

            return list(root)[0], d

        root , graph = preprocessing()

        def dfs(node, head):
            if node[1] == 1:
                head.left = TreeNode(node[0])
                head = head.left
            elif node[1] == 0:
                head.right = TreeNode(node[0])
                head = head.right

            if graph[node[0]] == []:
                return    
            
            # print(node, head)
            for i in graph[node[0]]:
                if i[1] == 1:
                    dfs(i, head)
                else:
                    dfs(i, head)

        head = TreeNode(root)
        sol = head
        dfs((root, 2), head)
        
        return sol
            




            