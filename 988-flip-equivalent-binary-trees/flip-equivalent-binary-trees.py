# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def rec(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
                
            if node1.val != node2.val:
                return False
            
            

            noswap = rec(node1.left, node2.left) and rec(node1.right, node2.right)
            swap = rec(node1.left, node2.right) and rec(node1.right, node2.left)

            return swap or noswap
            

        

        return rec(root1, root2)


        