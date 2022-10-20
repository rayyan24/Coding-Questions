# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
# copy the value of next node to cuurent node replace the next pointer of current node with next to next node

        n1 = node.next.next
        node.val = node.next.val
        node.next = n1
