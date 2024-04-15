# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        pths = []
        def dfs(node, path):
            if not node: return ""

            path += str(node.val)

            if not node.left and not node.right:
                pths.append(path)


            dfs(node.left, path)
            dfs(node.right, path)


        dfs(root, "")

        sol = 0
        for i in pths:
            sol += int(i)

        return sol

        