
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        left=head
        right=self.getMid(head)
        
#       right needs to be at next of middle Node
        
        temp=right.next
        right.next=None
        right=temp
#       recursive calls for left sub list and right sub list
        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge(left,right)
    def getMid(self,head):
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def merge(self,list1,list2):
        temp=dummy=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                temp.next=list1
                list1=list1.next
            else:
                temp.next=list2
                list2=list2.next
            temp=temp.next
        if list1:
            temp.next=list1
        if list2:
            temp.next=list2
        return dummy.next
    
        
        