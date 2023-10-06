# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = l1
        num1 = ""
        while (temp != None):
            num1 += str(temp.val)
            temp = temp.next
        num1 = int(num1)

        temp = l2
        num2 = ""
        while (temp != None):
            num2 += str(temp.val)
            temp = temp.next

        num2 = int(num2)
        sum = num1+num2
        sum = str(sum)
        head = ListNode()
        head.next = None
        temp = head
        size = len(sum)
        for i in range(size):
            if i == size-1:
                temp.val = sum[i]
                continue
            else:
                temp.val = sum[i]
                temp.next = ListNode()
                temp = temp.next

        return head
