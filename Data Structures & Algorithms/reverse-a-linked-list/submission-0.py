# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head 

        forward = head.next
        backward = head
        while forward:
            temp = forward.next
            forward.next = backward
            backward = forward 
            forward = temp
            
        head.next = None
        return backward 
        