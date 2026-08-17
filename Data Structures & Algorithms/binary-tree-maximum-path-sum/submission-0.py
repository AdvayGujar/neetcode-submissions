# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxPath = 0

    def maxPathForNode(self, root):
        tempValue = root.val

        if root.left and root.right:
            leftValue = self.maxPathForNode(root.left)
            rightValue = self.maxPathForNode(root.right)

            tempValue = max(tempValue, tempValue + rightValue + leftValue, tempValue + rightValue, tempValue + leftValue)

            self.maxPath = max(self.maxPath, tempValue)

            return max(root.val, root.val + leftValue, root.val + rightValue)
        elif root.right:
            rightValue = self.maxPathForNode(root.right)

            tempValue = max(tempValue + rightValue, tempValue)
            self.maxPath = max(self.maxPath, tempValue)

            return max(root.val, root.val + rightValue)
        elif root.left:
            leftValue = self.maxPathForNode(root.left)

            tempValue = max(tempValue + leftValue, tempValue)
            self.maxPath = max(self.maxPath, tempValue)

            return max(root.val, root.val + leftValue)

        self.maxPath = max(self.maxPath, tempValue)

        return tempValue

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = root.val
        self.maxPathForNode(root)

        return self.maxPath