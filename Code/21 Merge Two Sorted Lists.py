# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        if head1 == None and head2 == None:
            return
        arr = []
        temp = head1
        while temp != None:
            arr.append(temp.val)
            temp = temp.next
        temp = head2
        while temp != None:
            arr.append(temp.val)
            temp = temp.next
        arr.sort()
        head = ListNode()
        temp = head
        for i in range(len(arr)):
            if i == len(arr)-1:
                temp.val = arr[i]
            else:
                temp.val = arr[i]
                temp.next = ListNode()
                temp = temp.next
        return head
