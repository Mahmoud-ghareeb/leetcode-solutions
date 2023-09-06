# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = self.getLength(head)
        to_add = n%k
        size = n//k
        
        out = []
        cur = head
        for i in range(k):
            root = cur
            for j in range(size + (i < to_add) - 1):
                if cur: cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            out.append(root)

        return out

    def getLength(self, head):
        i = 0
        while head:
            i += 1
            head = head.next

        return i