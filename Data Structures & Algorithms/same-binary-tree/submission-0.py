# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class NodeMismatch(Exception):
    pass

class Solution:
    def isSameNode(self, p, q):
        if p.val != q.val:
            raise NodeMismatch()
            
        if p.left is not None and q.left is not None:
            self.isSameNode(p.left, q.left)
        elif p.left is None and q.left is None:
            pass
        else:
            raise NodeMismatch()

        if p.right is not None and q.right is not None:
            self.isSameNode(p.right, q.right)
        elif p.right is None and q.right is None:
            pass
        else:
            raise NodeMismatch()

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            pass
        else:
            return False

        try:
            self.isSameNode(p,q)
            return True

        except NodeMismatch:
            return False
