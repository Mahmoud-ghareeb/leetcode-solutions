# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        nums = set(nums)
        parent = ListNode()
        parent.next = head
        sol = parent
        while parent.next:
            if parent.next.val in nums:
                parent.next = parent.next.next
            else:
                parent = parent.next

        return sol.next




        