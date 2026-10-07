# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        curr = root

        while curr:
            if curr.left:
                # Find the rightmost node
                # in the left subtree
                prev = curr.left

                while prev.right:
                    prev = prev.right

                # Connect left subtree's rightmost node
                # to current node's right subtree
                prev.right = curr.right

                # Move left subtree to the right
                curr.right = curr.left

                # Remove left child
                curr.left = None

            # Move to next node
            curr = curr.right        