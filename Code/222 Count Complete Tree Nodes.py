# 222. Count Complete Tree Nodes
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getDepth(root,left=False,right=False):
            depth=1
            while root:
                root=root.left if left else root.right
                depth+=1
            return depth
        
        if root is None:
            return 0
        leftDepth=getDepth(root.left,left=True) # calculate the left depth
        rightDepth=getDepth(root.right,right=True) # calculate the right depth
# if true means tree is a perfect binary tree, number of nodes in perfect binary tree are (2**depth)-1
        if leftDepth==rightDepth:
            return (2**leftDepth)-1

        else:
            # +1 to accomdate the current level
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
        
