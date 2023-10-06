# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=float("-inf")
        def helper(root):
            nonlocal res
            if root is None:
                return 0
            leftMax=max(0,helper(root.left))
            rightMax=max(0,helper(root.right))            
            res=max(res,root.val+leftMax+rightMax)
            return root.val+max(leftMax,rightMax)
        helper(root)
        return res