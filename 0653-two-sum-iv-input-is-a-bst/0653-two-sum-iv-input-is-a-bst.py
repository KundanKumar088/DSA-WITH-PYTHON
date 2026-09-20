# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        seen = set()

        def dfs(node):
            if node is None:
                return False

            # Check whether the required value exists
            if k - node.val in seen:
                return True

            # Store current value
            seen.add(node.val)

            #search left and right subtree
            return dfs(node.left) or dfs(node.right)

        return dfs(root)             