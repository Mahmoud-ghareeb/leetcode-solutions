# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l = []
        while head:
            if head in l:
                return True
            l.append(head)
            head = head.next

        return False
        