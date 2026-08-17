# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create a hashmap for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            
            root_val = preorder[pre_start]
            node = TreeNode(root_val)
            
            # Find root in inorder
            root_idx = inorder_map[root_val]
            
            # Size of left subtree
            left_size = root_idx - in_start
            
            # Build left subtree
            node.left = build(
                pre_start + 1, 
                pre_start + left_size,
                in_start, 
                root_idx - 1
            )
            
            # Build right subtree
            node.right = build(
                pre_start + left_size + 1,
                pre_end,
                root_idx + 1,
                in_end
            )
            
            return node
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)