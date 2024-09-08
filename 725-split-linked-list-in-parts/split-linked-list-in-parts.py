# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        l = 0
        node = head
        while node:
            node = node.next
            l += 1
            
        per_list = l // k
        rem = l % k
        sol = []

        while k > 0:
            n = per_list
            if rem > 0:
                n += 1
                rem -= 1

            tmp = ListNode()
            tmp2 = tmp
            while head and n:
                tmp.next = head
                head = head.next
                tmp = tmp.next
                n -= 1

            tmp.next = None

            sol.append(tmp2.next)

            k -= 1


        return sol
        