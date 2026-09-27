# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        length = 0 
        ptr = head 
        while ptr: 
            ptr = ptr.next
            length += 1
        if length == n: return head.next 
        
        ptr = head
        i = length-n
        while i>1:
            ptr = ptr.next
            i -= 1


        ptr.next = ptr.next.next

        return head  
