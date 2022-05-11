# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #if we have an empty list 
        if not head:
            return None
        

        #for repeated
        while head.val == val:
            if not head.next:
                return None
            head = head.next
        
        # if it is the only one and its not our target
        if not head.next:
            return head                

        #to remove any element
        list_ptr = head
        while list_ptr.next:
            if list_ptr.next.val == val:
                list_ptr.next = list_ptr.next.next
            else:
                list_ptr = list_ptr.next    

        return head
                