
import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        # Available servers: min-heap
        free = list(range(k))
        heapq.heapify(free)

        # Busy servers: (finish_time, server_id)
        busy = []

        # Count requests handled by each server
        count = [0] * k

        for i in range(len(arrival)):
            current_time = arrival[i]

            # Release servers whose requests have finished
            while busy and busy[0][0] <= current_time:
                finish_time, server_id = heapq.heappop(busy)

                # Convert to circular-order virtual index
                virtual_id = i + (server_id - i) % k

                heapq.heappush(free, virtual_id)

            # If every server is busy, drop this request
            if not free:
                continue

            # Select the next available server
            virtual_id = heapq.heappop(free)
            server_id = virtual_id % k

            # Update request count
            count[server_id] += 1

            # Mark server as busy
            finish_time = current_time + load[i]
            heapq.heappush(busy, (finish_time, server_id))

        # Find maximum requests handled
        max_count = max(count)

        # Return all busiest servers
        return [
            i for i in range(k)
            if count[i] == max_count
        ]

        