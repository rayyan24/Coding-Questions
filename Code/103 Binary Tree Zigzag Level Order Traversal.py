# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         by default level order traversal goes from left to right
        res=[]
        queue=[root]
        flag=False
        while queue:
            size=len(queue)
            curLevel=[]
            for i in range(size):
                remNode=queue.pop(0)
                if remNode:
                    curLevel.append(remNode.val)
                    queue.append(remNode.left)
                    queue.append(remNode.right)
            if curLevel:
#               flag is true append in reverse 
                if flag:
                    res.append(curLevel[::-1])
                    flag=not flag
                # flag is false append as it is 
                else:
                    res.append(curLevel)
                    flag=not flag
        return res