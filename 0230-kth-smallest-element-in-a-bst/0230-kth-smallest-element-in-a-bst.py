# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack = []
        current = root

        while True:
            #Go as far left as possible

            while current:
                stack.append(current)
                current = current.left

            # visit the smallest remaining node
            current = stack.pop()
            k -= 1

            if k == 0:
                return current.val

            # Move to the right subtree
            current = current.right        