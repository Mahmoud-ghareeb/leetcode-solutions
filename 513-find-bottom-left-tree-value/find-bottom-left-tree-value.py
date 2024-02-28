# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        def dfs(node, depth):
            if not node: return 0

            depth += 1
            self.m = max(self.m, depth) 

            dfs(node.left, depth)
            dfs(node.right, depth)

            arr.append((node.val, depth))

        arr = []
        self.m = 0
        d = dfs(root, 0)
        
        for i in arr:
            if i[1] == self.m:
                return i[0]

        # return 0