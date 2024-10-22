# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        arr = []
        heapq.heapify(arr)

        q = deque()
        q.append((root, 0))

        tmp_lvl = 0
        s = 0

        while q:
            node, lvl = q.popleft()  
            if lvl == tmp_lvl:
                s += node.val
            else:
                heapq.heappush(arr, -1 * s)
                s = node.val
                tmp_lvl = lvl

            if node.left:
                q.append((node.left, lvl + 1))   
            if node.right:
                q.append((node.right, lvl + 1))

        if s > 0:
            heapq.heappush(arr, -1 * s)

        if k > len(arr):
            return -1

        # print(arr)

        for i in range(k-1):
            heapq.heappop(arr)

        return heapq.heappop(arr) * -1