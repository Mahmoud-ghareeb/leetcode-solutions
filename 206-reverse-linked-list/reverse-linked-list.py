# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head

        def rec(node, prev):
            if not node:
                return prev

            temp = ListNode(node.val, prev)
            prev = temp

            return rec(node.next, prev)

        return rec(head.next, ListNode(head.val))
            

            


        