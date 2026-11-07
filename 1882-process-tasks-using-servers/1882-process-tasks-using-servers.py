class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:



        available = []
        busy = []

        # Add all servers to available heap
        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))

        ans = []
        current_time = 0

        for i, duration in enumerate(tasks):

            # Task arrives at second i
            current_time = max(current_time, i)

            # Release servers that have finished
            while busy and busy[0][0] <= current_time:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If no server is available, wait
            if not available:
                current_time = busy[0][0]

                # Release all servers finishing now
                while busy and busy[0][0] <= current_time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            # Select the best available server
            weight, index = heapq.heappop(available)

            ans.append(index)

            # Calculate when the server becomes free
            finish_time = current_time + duration

            heapq.heappush(
                busy,
                (finish_time, weight, index)
            )

        return ans
        