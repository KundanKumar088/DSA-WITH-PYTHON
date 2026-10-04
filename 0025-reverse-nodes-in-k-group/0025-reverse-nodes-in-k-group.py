# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:

        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:
            # Find the kth node
            kth = group_prev

            for _ in range(k):
                kth = kth.next

                if kth is None:
                    return dummy.next

            # Save the node after the group
            group_next = kth.next

            # Reverse the group
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Connect previous part to reversed group
            old_group_start = group_prev.next
            group_prev.next = kth

            # Move group_prev to the end of reversed group
            group_prev = old_group_start        