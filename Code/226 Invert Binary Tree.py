# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
#         swapping the current node
        root.left,root.right=root.right,root.left
#         calling the same function for left and right childs
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root