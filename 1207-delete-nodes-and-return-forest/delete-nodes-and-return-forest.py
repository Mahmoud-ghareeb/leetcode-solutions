# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        to_delete_d = {}
        for i in to_delete:
            to_delete_d[i] = 1

        roots = [root]
        sol = {root:0}
        self.is_r = False

        def dfs(node, parent, dire):
            if not node:
                return 

            candidate = to_delete_d.get(node.val, None)
            if candidate:
                
                if sol.get(node, None):
                    del sol[node]

                if node.val == root.val:
                    self.is_r = True

                if node.left:
                    roots.append(node.left)
                    sol[node.left] = 1
                if node.right:
                    roots.append(node.right)
                    sol[node.right] = 1
                    
                if parent is not None:
                    if dire == 'l':
                        parent.left = None
                    else:
                        parent.right = None

            dfs(node.left, node, 'l')
            dfs(node.right, node, 'r')

        for node in roots:
            dfs(node, None, None)

        sol = list(sol.keys())
        return sol[1:] if self.is_r else sol
            
        