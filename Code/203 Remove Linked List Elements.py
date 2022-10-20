# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None: return 
        dummy=ListNode()
        dummy.next=head
        temp=dummy
        while temp:
            if temp.next and temp.next.val==val:
                temp.next=temp.next.next
# increment temp only when next.val is not the value to be removed.this ensures that temp is never pointing at the node to be deleted
            else:
                temp=temp.next
        return dummy.next