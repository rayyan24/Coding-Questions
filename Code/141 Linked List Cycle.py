# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # arr={}
        # counter=0
        # temp=head
        # while(temp!=None):
        #     if temp in arr:
        #         return True
        #     else:
        #         arr[temp]=counter
        #         counter+=1
        #         temp=temp.next
        # return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
