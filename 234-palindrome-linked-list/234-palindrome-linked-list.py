# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        #get the middle which is the slow
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse from the middle
        prev = None
        nprev = None
        while slow:
            nprev = slow.next
            slow.next = prev
            prev = slow
            slow = nprev
            
        #check if palindrom
        left = head
        right = prev
        
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True
        
        
        
        
        
        
        
        
        
        
        
        