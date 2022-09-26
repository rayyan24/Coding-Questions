# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(lb,ub,arr):
            while lb<ub:
                arr[lb],arr[ub]=arr[ub],arr[lb]
                lb+=1
                ub-=1
        temp=head
        arr=[]
        while temp!=None:
            arr.append(temp.val)
            temp=temp.next
        lb=0
#       -1 to adjust with zero based indexing
        ub=lb+k-1
        while ub<len(arr):
            reverse(lb,ub,arr)
            lb=ub+1
            ub=lb+k-1
        temp=head
        for i in arr:
            temp.val=i
            temp=temp.next
        return head
            
        