# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        arr = []
        temp = head
        while temp != None:
            arr.append(temp.val)
            temp = temp.next
        arr = arr[::-1]
        HEAD = ListNode()
        temp = HEAD
        for i in range(len(arr)):
            if i == len(arr)-1:
                temp.val = arr[i]
            else:
                temp.val = arr[i]
                temp.next = ListNode()
                temp = temp.next
        temp = HEAD
        return HEAD
