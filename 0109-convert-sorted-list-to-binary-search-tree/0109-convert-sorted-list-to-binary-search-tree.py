# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:



        def build(start, end):
            if start == end:
                return None

            slow = fast = start

            while fast != end and fast.next != end:
                slow = slow.next
                fast = fast.next.next

            root = TreeNode(slow.val)

            root.left = build(start, slow)
            root.right = build(slow.next, end)

            return root

        return build(head, None)
        