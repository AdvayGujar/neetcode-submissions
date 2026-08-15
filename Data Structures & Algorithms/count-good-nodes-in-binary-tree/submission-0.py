# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    good = 0

    def nodes(self,root, maxValue):
        if root.val >= maxValue:
            self.good += 1
            maxValue = root.val
        
        if root.left:
            self.nodes(root.left, maxValue)
        if root.right:
            self.nodes(root.right, maxValue)

    def goodNodes(self, root: TreeNode) -> int:
        self.nodes(root, root.val)

        return self.good