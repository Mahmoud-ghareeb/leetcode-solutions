# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left = root)

        def dfs(node, dpth):
            if not node: return 0

            if dpth == depth-1:
                curr = TreeNode(val)
                temp = node.left
                node.left = curr
                curr.left = temp

                curr = TreeNode(val)
                temp = node.right
                node.right = curr
                curr.right = temp

            dpth += 1 

            dfs(node.left, dpth)
            dfs(node.right, dpth)

        dfs(root, 1)

        return root
        