# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr=[]
        def inorder(root):
            if root.left is not None:
                inorder(root.left)
            arr.append(root.val)
            if root.right is not None:
                inorder(root.right)
        inorder(root)
        # print(arr)
        return arr[k-1]