# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class ValidBSTError(Exception):
    pass

class Solution:
    def validNode(self, root, leftLimit, rightLimit):
        if root.left:
            if leftLimit < root.left.val < root.val:
                self.validNode(root.left, leftLimit, root.val)
            else:
                raise ValidBSTError()
        
        if root.right:
            if root.val < root.right.val < rightLimit:
                self.validNode(root.right, root.val, rightLimit)
            else:
                raise ValidBSTError()

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        try:
            self.validNode(root, float('-inf'), float('inf'))
            return True
        except ValidBSTError:
            return False