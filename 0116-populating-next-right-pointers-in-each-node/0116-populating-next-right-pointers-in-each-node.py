"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':


        if not root:
            return None

        level = root

        while level.left:
            current = level

            while current:
                # Connect left child to right child
                current.left.next = current.right

                # Connect right child to the next
                # parent's left child, if one exists
                if current.next:
                    current.right.next = current.next.left

                current = current.next

            # Move to the next level
            level = level.left

        return root
        