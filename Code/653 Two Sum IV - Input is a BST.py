# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # As you traverse the tree, put each node's value into a set. In order for some value x to sum up to k, the value k - x must have been in the set already. Therefore, assuming we have a set of node values, if we find a complement of a node in that set, we have found two values that sum up to k.
    def findTarget(self, root: Optional[TreeNode], mainTarget: int) -> bool:
        Set=set()
        def helper(root,target):
            if root is None:
                return False
            curTarget=mainTarget-root.val
            if curTarget in Set:
                return True 
            Set.add(root.val)
            return helper(root.left,mainTarget) or helper(root.right,mainTarget)
        return helper(root,mainTarget)
        