# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isTree(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        elif (root is None and subRoot is not None) or (root is not None and subRoot is None):
            return False

        if root.val != subRoot.val:
            return False
        
        if not self.isTree(root.left, subRoot.left):
            return False
        if not self.isTree(root.right, subRoot.right):
            return False

        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        if root.val == subRoot.val:
            if self.isTree(root, subRoot):
                return True

        if self.isSubtree(root.left, subRoot):
            return True
        if self.isSubtree(root.right, subRoot):
            return True

        return False