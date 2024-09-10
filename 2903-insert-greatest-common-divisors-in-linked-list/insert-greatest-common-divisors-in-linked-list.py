# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def gcd(i, j):
            while j != 0:
                r = i//j
                b = i%j
                i = j
                j = b

            return i

        node = head

        while node.next:
            i = node.val
            j = node.next.val
            tmp = gcd(max(i, j), min(i, j))

            tmp_node = ListNode(tmp)
            tmp_node.next = node.next

            node.next = tmp_node

            node = node.next.next


        return head

        