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

        reversed_linked_list = ListNode(head.val)
    
        while head.next:
            head = head.next
            node = ListNode(head.val, reversed_linked_list)
            reversed_linked_list = node
        return reversed_linked_list
            

            


        