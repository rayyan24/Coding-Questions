# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        def helper(root,target):
            if root is None:
                return False         
            # when current node is a leaf node and current nodes value is equal to the required value
            if root.left is None and root.right is None and root.val==target:
                return True
            return helper(root.left,target-root.val) or helper(root.right,target-root.val)
        return helper(root,target)