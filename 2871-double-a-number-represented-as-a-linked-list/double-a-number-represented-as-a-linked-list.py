# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse_linked_list(node):

            prev = None
            curr = node
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        head = reverse_linked_list(head)
        
        node = head
        prev = ListNode(0, next=node)
        rem = 0
        while node:
            temp = 2 * node.val + rem
            val = temp % 10
            rem = (temp - val)//10

            node.val = val
            node = node.next
            prev = prev.next

        if rem > 0:
            new_node = ListNode(rem)
            prev.next = new_node

        return reverse_linked_list(head)