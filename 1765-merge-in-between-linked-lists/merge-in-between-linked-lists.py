# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        p1 = list1
        i = 1
        while i<a:
            p1 = p1.next
            i += 1

        j = 0
        temp = p1
        while j<b-a+2:
            temp = temp.next
            j += 1

        p1.next = list2
        while list2.next:
            list2 = list2.next

        list2.next = temp

        return  list1

        



        