# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        center = head
        ncurr = head
        
        while center:
            ncurr = ncurr.next
            center.next = pre
            pre = center
            center = ncurr
        return pre
                

        
            