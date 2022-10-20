# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = {}
        counter = 0
        temp = head
        while (temp != None):
            if temp in arr:
                return temp
            else:
                arr[temp] = counter
                counter += 1
                temp = temp.next
        return None
