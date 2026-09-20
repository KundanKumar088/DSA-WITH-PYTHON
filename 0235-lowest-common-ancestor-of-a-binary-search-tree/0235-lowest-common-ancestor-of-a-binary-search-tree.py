# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:

            if p.val < root.val and q.val < root.val:
                # both nodes are in the left subtree
                root = root.left

            elif p.val > root.val and q.val > root.val:
                # both nodesm are in the right subtree
                root = root.right
            else:
                # they are on diff sides
                # or root is p/q itself
                return root        
