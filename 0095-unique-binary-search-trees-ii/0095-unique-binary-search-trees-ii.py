# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# LeetCode provides the TreeNode definition.

class Solution:
    def generateTrees(self, n: int):
        def build(start, end):
            # An empty range represents an empty subtree.
            if start > end:
                return [None]

            trees = []

            # Try every value as the root.
            for root_val in range(start, end + 1):
                left_trees = build(start, root_val - 1)
                right_trees = build(root_val + 1, end)

                # Combine every left subtree with every right subtree.
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        trees.append(root)

            return trees

        return build(1, n)