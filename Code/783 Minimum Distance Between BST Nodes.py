# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res=float("inf")
        prev=None
        def helper(root):
            nonlocal res,prev
            if root is None:
                return
            helper(root.left)
            if prev is not None:
                res=min(res,root.val-prev)
            prev=root.val
            helper(root.right)
        helper(root)
        return res
        