# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self,root):
        arr=[]
        def helper(root):
            if root.left is not None:
                helper(root.left)
            arr.append(root.val)
            if root.right is not None:
                helper(root.right)
        helper(root)
        return arr
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
# traverse inorder and store the result in array check if sorted if true return true  else return false 
            arr=self.inOrder(root)
            print(arr)
            for i in range(len(arr)-1):
                if arr[i]>=arr[i+1]:
                    return False
            return True