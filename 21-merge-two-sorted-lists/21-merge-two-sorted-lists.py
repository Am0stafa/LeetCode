# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode(0)
        tail = output
        l1 = list1
        l2 = list2
        
        while l1 != None and l2 is not None :
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
            
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
            
        return output.next
        