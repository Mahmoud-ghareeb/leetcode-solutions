# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def rec(node, ans, flag):
            if not node: return 0

            if node.left==None and node.right==None and flag=="yes":
                self.ans += node.val

            # print(node.val, ans, flag, node.left, node.right)

            rec(node.left, ans, "yes")
            rec(node.right, ans, "no")

        rec(root, 0, "no")
        return self.ans
        