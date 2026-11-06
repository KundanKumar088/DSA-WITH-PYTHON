# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:


        def build(left, right):

            # Base condition
            if left > right:
                return None

            # Find middle index
            mid = (left + right) // 2

            # Create root node
            root = TreeNode(nums[mid])

            # Build left subtree
            root.left = build(left, mid - 1)

            # Build right subtree
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)
        