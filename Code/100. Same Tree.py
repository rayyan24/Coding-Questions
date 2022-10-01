# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        BASE CAES of dfs function
        root1 is none and root 2 is not none (reverse also)-->false
        root1 is none or root2 is none --> true
        root1.val in not root.val --->
        return dfs(left) and dfs(right)
        '''
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None or root1.val!=root2.val:
            return False
        return self.isSameTree(root1.left,root2.left) and self.isSameTree(root1.right,root2.right)

        