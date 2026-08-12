# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxLength = 0

    def diameter(self, root):
        left = 0
        right = 0

        if root.left:
            left = 1 + self.diameter(root.left)
        if root.right:
            right = 1 + self.diameter(root.right)

        self.maxLength = max(self.maxLength, left + right)

        return max(left,right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter(root)

        return self.maxLength