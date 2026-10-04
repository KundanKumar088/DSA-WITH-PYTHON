# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = []

        for i , node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val, i, node))

        dummy  = ListNode(0)

        current = dummy

        while heap:
            value , i , node = heapq.heappop(heap)


            current.next = node
            current = current.next

            # add next node from the same list

            if node.next:
                heapq.heappush(
                    heap,
                    (node.next.val, i , node.next)
                )           

        return dummy.next        