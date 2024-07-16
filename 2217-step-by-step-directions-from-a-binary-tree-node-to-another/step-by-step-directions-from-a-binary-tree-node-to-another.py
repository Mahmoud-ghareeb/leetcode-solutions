# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def get_path(target):

            def bfs(node):
                q = deque()
                q.append([node, ''])

                while len(q) > 0:
                    node, route = q.popleft()
                    if node.val == target:
                        return route

                    if node.left is not None:
                        q.append([node.left, route+'L'])
                    
                    if node.right is not None:
                        q.append([node.right, route+'R'])

            return bfs(root)
        
        fdist = get_path(startValue)
        tdist = get_path(destValue)
        m, n = len(fdist), len(tdist)
        sol = ""
        i = 0
        while i<m and i<n:
            if fdist[i] == tdist[i]:
                i += 1
                continue
            break

        return 'U'*(len(fdist)-i)+tdist[i:]