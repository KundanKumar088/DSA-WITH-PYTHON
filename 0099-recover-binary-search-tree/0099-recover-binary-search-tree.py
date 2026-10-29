# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root) -> None:
        first = None
        second = None
        prev = None

        stack = []
        curr = root

        # Iterative inorder traversal
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # Detect an incorrect inorder order
            if prev and prev.val > curr.val:
                if first is None:
                    first = prev
                second = curr

            prev = curr
            curr = curr.right

        # Restore the BST by swapping values
        first.val, second.val = second.val, first.val

        