# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        q = deque()
        lvl = 0
        q.appendleft([root, lvl])
        node = root
        d = defaultdict(list)
        while q:
            temp, lvl = q.pop()
            if not temp : continue
            if lvl%2 == 0:
                if temp.val%2 == 0:
                    print("1", lvl, temp)
                    return False
            else:
                if temp.val%2 != 0:
                    return False

            try:      
                prev = d[lvl][-1]
                if lvl%2 == 0:
                    if temp.val <= prev:
                        return False
                else:
                    if temp.val >= prev:
                        return False
            except:
                pass
                
            d[lvl].append(temp.val)

            if node.left:
                q.appendleft([temp.left, lvl+1])
            if node.right:
                q.appendleft([temp.right, lvl+1])

        return True

        