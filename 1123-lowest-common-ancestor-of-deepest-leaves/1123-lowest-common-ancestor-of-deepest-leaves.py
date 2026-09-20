# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:
        def dfs(node):

            #empty tree
            if node is None:
                return 0, None


            # get information from left and right subtrees
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            #left subtree is deeper
            if left_depth > right_depth:
                return left_depth + 1 , left_lca

            # right subtree is deeper
            elif right_depth > left_depth:
                return right_depth + 1, right_lca

            #both sides have deepest leaves
            else:
                return left_depth + 1 , node

        return dfs(root)[1]                      