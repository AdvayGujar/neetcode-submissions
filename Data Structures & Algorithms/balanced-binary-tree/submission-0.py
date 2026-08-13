# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FoundTargetException(Exception):
    pass

class Solution:
    def balanced(self, root):
        left = 0
        right = 0

        if root.left is not None:
            left = 1 + self.balanced(root.left)

        if root.right is not None:
            right = 1 + self.balanced(root.right)

        if (left - right) < -1 or (left - right) > 1:
            raise FoundTargetException()

        return max(left , right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        try:
            self.balanced(root)
            return True
        except FoundTargetException:
            return False