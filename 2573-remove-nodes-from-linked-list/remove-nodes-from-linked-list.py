# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse_linked_list(head):
            curr = None
            node = head
            while node:
                temp = node.next
                node.next = curr
                curr = node
                node = temp

            return curr
        
        head = reverse_linked_list(head)
        max_val = 0
        node = head
        temp = head
        while node:
            max_val = max(max_val, node.val)
            if node.val < max_val:
                temp.next = node.next
            else:
                temp = node
            
            node = node.next

        head = reverse_linked_list(head)

        return head



        