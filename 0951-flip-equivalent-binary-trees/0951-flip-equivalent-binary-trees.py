# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        #both nodes are empty
        if root1 is None and root2 is None:
            return True

        # one node is empty 
        if root1 is None or root2 is None:
            return False

        #values are diff
        if root1.val != root2.val:
            return False

        # option 1: Dont flip
        no_flip = (
            self.flipEquiv(root1.left, root2.left)
            and 
            self.flipEquiv(root1.right, root2.right)
        )  

        #option 2: flip
        flip = (
            self.flipEquiv(root1.left, root2.right)
            and 
            self.flipEquiv(root1.right, root2.left)
        )  


        return no_flip or flip        