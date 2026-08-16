# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FoundTheNumber(Exception):
    pass

class Solution:
    noOfNodes = 0
    kSmallest = None

    def inorder(self, root):
        if root.left:
            self.inorder(root.left)
        
        self.noOfNodes -= 1
        if self.noOfNodes == 0:
            self.kSmallest = root.val
            raise FoundTheNumber()
        
        if root.right:
            self.inorder(root.right)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.noOfNodes = k

        try:
            self.inorder(root)
        except FoundTheNumber:
            return self.kSmallest