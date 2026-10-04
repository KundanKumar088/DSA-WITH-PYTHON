# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # create a gap of n + 1 nodes
        for _ in range (n + 1):
            fast = fast.next

        #move both pointers
        while fast:
            slow = slow.next
            fast = fast.next

        # remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next        