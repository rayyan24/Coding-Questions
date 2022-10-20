# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # temp=head
        # counter=0
        # while temp!=None:
        #     counter+=1
        #     temp=temp.next
        # toRemove=counter-n
        # temp=head
        # for i in range(toRemove-1):
        #     temp=temp.next
        # if temp.next!=None:
        #     temp.next=temp.next.next
        #     return head
        # return None

        # left=head
        # right=head
        # while(right is not None and n!=0):
        #     right=right.next
        #     n-=1
        # while right is not None:
        #     left=left.next
        #     right=right.next
        # if left.next!=None:
        #     left.next=left.next.next
        #     return head
        # else:
        #     return
        temp = ListNode(0, head)
        left = temp
        right = head
        # while right is not None and n!=0:
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return temp.next
