# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        @cache
        def dfs(node, ptr):
            if not node: 
                return False
            
            if ptr.val == node.val and not ptr.next:
                return True
            
            if node.val == ptr.val:
                if dfs(node.left, ptr.next) or dfs(node.right, ptr.next):
                    return True
            
            return dfs(node.left, head) or dfs(node.right, head)

        return dfs(root, head)






        