# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subroot is empty , it is always a subtree
        if subRoot is None:
            return True

        # rootis empty but subroot is not
        if root is None:
            return False

        # check if trees starting here are identical
        if self.isSameTree(root, subRoot):
            return True


        #Search in left and right subtrees
        return (
            self.isSubtree(root.left, subRoot)
            or
            self.isSubtree(root.right,subRoot)
        )        
    def isSameTree(self,p,q):
        #both are empty
        if p is None and q is None:
            return True

        # one is empty
        if p is None or q is None:
            return False

        #values are diff
        if p.val != q.val:
            return False

        #comapre corresponding children
        return(
            self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right)
        )        
