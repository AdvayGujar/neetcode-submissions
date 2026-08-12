# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    length = 1
    maximum = 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.left is not None:
            self.length += 1
            self.maximum = max(self.length, self.maximum)
            self.maxDepth(root.left)
            self.length -= 1
        
        if root.right is not None:
            self.length += 1
            self.maximum = max(self.length, self.maximum)
            self.maxDepth(root.right)
            self.length -= 1

        return self.maximum