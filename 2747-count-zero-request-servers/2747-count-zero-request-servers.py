class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:



        # Sort logs by time
        logs.sort(key=lambda log: log[1])

        # Preserve original query indices
        sorted_queries = sorted(
            (q, i) for i, q in enumerate(queries)
        )

        ans = [0] * len(queries)

        # Frequency of each active server
        server_count = defaultdict(int)

        left = 0
        right = 0
        m = len(logs)

        for q, idx in sorted_queries:

            start = q - x

            # Add logs within the right boundary
            while right < m and logs[right][1] <= q:
                server_id = logs[right][0]
                server_count[server_id] += 1
                right += 1

            # Remove logs outside the left boundary
            while left < right and logs[left][1] < start:
                server_id = logs[left][0]

                server_count[server_id] -= 1

                if server_count[server_id] == 0:
                    del server_count[server_id]

                left += 1

            # Servers without requests
            ans[idx] = n - len(server_count)

        return ans
        