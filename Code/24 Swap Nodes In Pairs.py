# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        left = head
        right = head.next
        while True:
            left.val, right.val = right.val, left.val
            left = left.next.next
            if right.next and right.next.next:
                right = right.next.next
            else:
                break
        return head
