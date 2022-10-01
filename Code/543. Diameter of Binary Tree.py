# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        Max=0
        # ****543. Diameter of Binary Tree********
        
        def helper(root):
#           height of a null tree is -1.-1 is height 
            if root is None:
                return -1
#             left and right are the heights of left and right subtrees
            left=helper(root.left)
            right=helper(root.right)
#         left+right+2 gives the height of subtrees and this gives the diameter of current node
            Max=max(Max,left+right+2)
#     +1 to adjust a edge and also to cancel out -1 when current node is a leaf node 
            return 1+max(left,right)