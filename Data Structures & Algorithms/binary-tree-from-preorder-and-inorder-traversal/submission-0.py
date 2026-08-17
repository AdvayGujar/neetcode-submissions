# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        node = TreeNode(preorder[0])
        index = inorder.index(node.val)
        leftTreeLength = index
        rightTreeLength = len(preorder) - (index + 1)
        #left subtree
        if leftTreeLength > 0:
            node.left = self.buildTree(preorder[1:leftTreeLength + 1], inorder[0:index])

        #right subtree
        if rightTreeLength > 0:
            node.right = self.buildTree(preorder[leftTreeLength + 1:], inorder[index + 1:])

        return node