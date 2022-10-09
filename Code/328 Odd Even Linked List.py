# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        next of odd will always be even 
        next of even will always be odd
        odd and even will never colide 
        '''
        if head is None:
            return head
        odd=head
        even=head.next
        evenHead=even
        while even and even.next :
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=evenHead
#         orignal linked list is modified
        return head
        