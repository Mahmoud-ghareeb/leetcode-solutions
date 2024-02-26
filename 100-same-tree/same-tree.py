# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def in_order(node, sol):
            if not node: 
                sol.append('-1')
                return

            sol.append(node.val)

            in_order(node.left, sol)
            in_order(node.right, sol)

            return sol

        arr1 = in_order(p, [])
        arr2 = in_order(q, [])

        return arr1 == arr2
        