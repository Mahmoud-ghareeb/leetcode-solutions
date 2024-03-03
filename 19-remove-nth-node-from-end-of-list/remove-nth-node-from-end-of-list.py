# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        node1 = dummy
        node2 = dummy
        # n -= 1
        while node2:
            if n < 0:
                node1 = node1.next
            else:
                n -= 1

            node2 = node2.next
        
        if node1.next == None:
            return node1.next

        try:
            node1.next = node1.next.next
        except:
            pass

        return dummy.next


        