# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     ****572. Subtree of Another Tree*****
    def isSubtree(self, main: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
        '''
        sub--> none main can be anything return true
        main--> none and sub is not none return false 
        '''
        if sub is None: return True
        if main is None: return False
#         oredr of above two statements is important
        if self.isSameTree(main,sub):
            return True
        return self.isSubtree(main.left,sub) or self.isSubtree(main.right,sub)
        
    def isSameTree(self,main,sub):
        if main is None and sub is None:
            return True
        if main is not None and sub is not None and main.val==sub.val:
            return(self.isSameTree(main.left,sub.left) and self.isSameTree(main.right,sub.right))
        return False