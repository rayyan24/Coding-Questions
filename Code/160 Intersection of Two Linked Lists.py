# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        Set=set()
        temp=head1
        while temp:
            Set.add(temp)
            temp=temp.next
        temp=head2
        while temp:
            if temp in Set:
                return temp
            temp=temp.next
        return None
