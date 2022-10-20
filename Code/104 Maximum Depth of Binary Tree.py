# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Max=-1
        def helper(root,cur_dep):
            if root is None:
                return cur_dep
            
            Max=max(helper(root.left,cur_dep+1),helper(root.right,cur_dep+1))
            return Max
        return helper(root,0)
        