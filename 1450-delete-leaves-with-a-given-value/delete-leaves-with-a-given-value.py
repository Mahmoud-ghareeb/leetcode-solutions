# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(node, parent, drc):
            if not node: return

            dfs(node.left, node, 'left')
            dfs(node.right, node, 'right')

            if node.left == None and node.right == None and node.val == target:
                if drc == 'left':
                    parent.left = None
                elif drc == 'right' :
                    parent.right = None
                else:
                    node.val = None
                    return None

        dfs(root, None, None)
        return root if root.val != None else None


            