# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        '''
        helper returns an array of two elements
        zero th element is bool weather the current node is balanced or not
        first element is an integer which tells the height of this node
        '''
        def helper(root):
            
            if root is None:
                return[True,0]
            LEFT,RIGHT=helper(root.left),helper(root.right)
            isBalanced=LEFT[0] is True and RIGHT[0] is True and abs(LEFT[1]-RIGHT[1])<=1
            return [isBalanced,1+max(LEFT[1],RIGHT[1])]
        return helper(root)[0]
        
        
        
        
        
        