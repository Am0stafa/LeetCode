# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n ==1:
            return ListNode().next
            
        dummyHead = ListNode()
        dummyHead.next = head
        #get the length
        a = head
        len = 0
        while a:
            len+=1
            a = a.next
        pos = (len - n )
        
        if n == len:
            head=head.next
            return head
        
        while head:
            if pos == 1:
                if head.next:
                    head.next = head.next.next
            head = head.next
            pos-=1
        
        
        
        
        return dummyHead.next
        