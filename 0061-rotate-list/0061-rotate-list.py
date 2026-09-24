# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head

        # Find length and last node
        n = 1
        tail = head

        while tail.next:
            tail = tail.next
            n += 1

        # Remove unnecessary full rotations
        k = k % n

        if k == 0:
            return head

        # Make the list circular
        tail.next = head

        # Find the new tail
        steps = n - k

        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        # New head is after new tail
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head