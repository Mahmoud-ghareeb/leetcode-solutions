# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head.next:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        rev = self.reverse(slow.next)

        p1 = head
        p2 = rev

        while p1 and p2:
            temp_p1 = p1.next
            temp_p2 = p2.next

            p1.next = p2
            p2.next = temp_p1

            p1 = temp_p1
            p2 = temp_p2

        p1.next = None

        return head


    def reverse(self, head):
        if not head.next:
            return head

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev




        