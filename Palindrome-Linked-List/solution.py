# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            
        rev = None
        while slow:
            temp = slow.next
            slow.next = rev
            rev = slow
            slow = temp
            
        while rev:
            if(rev.val != head.val):
                return False
            
            rev = rev.next
            head = head.next
            
        return True