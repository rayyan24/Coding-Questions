# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # L N R
        if root == None:
            return []
        ans = []

        def helper(root):
            if root.left != None:
                helper(root.left)
            ans.append(root.val)
            if root.right != None:
                helper(root.right)
        helper(root)
        return (ans)
