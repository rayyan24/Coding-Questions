# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        num = ""
        while (temp != None):
            num += str(temp.val)
            temp = temp.next
        if num == num[::-1]:
            return True
        return False
