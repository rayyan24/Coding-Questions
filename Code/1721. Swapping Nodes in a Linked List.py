# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if head==None:return
#         count=1
#         temp=head
#         while True:
#             if temp.next==None:
#                 break
#             temp=temp.next
#             count+=1
#         begInd=k
#         begVal=-1
#         # endInd=count-k+1 if count%k!=0 else k
#         endInd=k if count==k else count-k+1
#         endVal=-1
#         temp=head
#         i=1
#         while temp:
#             if i==begInd:
#                 begVal=temp.val
#             if i==endInd:
#                 endVal=temp.val
#                 temp.val=begVal
#             i+=1
#             temp=temp.next
#         i=1
#         temp=head
#         while True:
#             if i==begInd:
#                 temp.val=endVal
#                 break
#             i+=1
#             temp=temp.next
#         return head
class Solution:
    def swapNodes(self, head , k) :
        fast_point = head
        slow_point = None
        beg_point = None
        index = 1
        while fast_point is not None:
# when fast pointer is on k we will start the slow pointer and initialize beg_pointer to this node this condition will be true only once
            if index == k:
                beg_point = fast_point
                slow_point = head
            elif slow_point is not None:
                slow_point = slow_point.next
            fast_point = fast_point.next
            index += 1
#when the loop terminates begPointer will be at beg node which is to be swapped and slow pointer will be at end node which is to be swapped
        beg_point.val, slow_point.val = slow_point.val, beg_point.val
        return head
            
        
        