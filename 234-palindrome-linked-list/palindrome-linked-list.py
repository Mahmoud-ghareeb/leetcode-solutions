# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        s = []

        while head.next:
            s.append(head.val)
            head = head.next
        s.append(head.val)

        n = len(s)

        if n%2 == 0:
            lt = n//2 - 1
            rt = n//2
        else:
            lt = n//2
            rt = n//2
            
        while lt>=0:
            if s[lt] != s[rt]:
                return False
            lt -=  1
            rt += 1


        return True


        

        
        
        