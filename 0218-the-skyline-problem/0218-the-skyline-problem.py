import heapq

class Solution:
    def getSkyline(self, buildings):
        # (x, height, right)
        events = []

        for left, right, height in buildings:
            # Start event: negative height
            events.append((left, -height, right))

            # End event: positive height
            events.append((right, height, 0))

        # Sorting automatically gives:
        # 1. Smaller x first
        # 2. At same x:
        #    - starts before ends
        #    - taller starts before shorter starts
        #    - shorter ends before taller ends
        events.sort()

        # Max heap using negative heights.
        # (negative_height, right)
        heap = [(0, float('inf'))]

        result = []
        prev_height = 0

        for x, height, right in events:

            # Remove buildings that have already ended.
            while heap[0][1] <= x:
                heapq.heappop(heap)

            if height < 0:
                # Building starts
                heapq.heappush(heap, (height, right))

            else:
                # Building ends.
                # We don't remove it directly because heapq
                # doesn't support efficient arbitrary deletion.
                #
                # Marking/removing by height requires a different
                # data structure, so use lazy deletion below.
                pass

            current_height = -heap[0][0]

            if current_height != prev_height:
                result.append([x, current_height])
                prev_height = current_height

        return result