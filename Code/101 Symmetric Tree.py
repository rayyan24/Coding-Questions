# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# ************** 101. Symmetric Tree******************
 # Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
class Solution:
    def helper(self,t1,t2):
#         if any one of them is none return weather both are none or not
        if t1 is None or t2 is None:
            return (t1==t2)
        if t1.val!=t2.val:
            return False
        return (self.helper(t1.left,t2.right) and self.helper(t1.right,t2.left))
        
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.helper(root.left,root.right)