# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         BFS algo for level order traversal
        res=[]
        queue=[root]
        while queue:
            size=len(queue)
            curLevel=[]
            for i in range(size):
                remNode=queue.pop(0) # pop the current node and add its children to the queue 
                if remNode:
                    curLevel.append(remNode.val)
                    queue.append(remNode.left)
                    queue.append(remNode.right)
            if curLevel:
                res.append(curLevel)
        return res[::-1]