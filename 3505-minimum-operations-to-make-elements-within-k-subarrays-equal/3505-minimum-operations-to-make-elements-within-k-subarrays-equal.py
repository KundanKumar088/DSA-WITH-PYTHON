


class SlidingMedian:
    def __init__(self):
        self.small = []  # Max heap (negative values)
        self.large = []  # Min heap

        self.delayed = defaultdict(int)

        self.small_size = 0
        self.large_size = 0

        self.small_sum = 0
        self.large_sum = 0

    def prune(self, heap):
        while heap:
            num = -heap[0] if heap is self.small else heap[0]

            if self.delayed[num] == 0:
                break

            heapq.heappop(heap)
            self.delayed[num] -= 1

    def rebalance(self):
        self.prune(self.small)
        self.prune(self.large)

        # Small heap can have at most one extra element
        while self.small_size > self.large_size + 1:
            val = -heapq.heappop(self.small)

            self.small_size -= 1
            self.small_sum -= val

            heapq.heappush(self.large, val)

            self.large_size += 1
            self.large_sum += val

            self.prune(self.small)

        while self.small_size < self.large_size:
            val = heapq.heappop(self.large)

            self.large_size -= 1
            self.large_sum -= val

            heapq.heappush(self.small, -val)

            self.small_size += 1
            self.small_sum += val

            self.prune(self.large)

    def add(self, num):
        self.prune(self.small)

        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
            self.small_sum += num
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
            self.large_sum += num

        self.rebalance()

    def remove(self, num):
        self.prune(self.small)
        self.prune(self.large)

        median = -self.small[0]
        self.delayed[num] += 1

        if num <= median:
            self.small_size -= 1
            self.small_sum -= num

            if num == median:
                self.prune(self.small)
        else:
            self.large_size -= 1
            self.large_sum -= num

            if self.large and num == self.large[0]:
                self.prune(self.large)

        self.rebalance()

    def get_cost(self):
        self.prune(self.small)
        self.prune(self.large)

        median = -self.small[0]

        left_cost = (
            median * self.small_size - self.small_sum
        )

        right_cost = (
            self.large_sum - median * self.large_size
        )

        return left_cost + right_cost


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:

        n = len(nums)

        maritovexi = nums

        # Part 1: Calculate cost of every window
        sm = SlidingMedian()

        for i in range(x):
            sm.add(nums[i])

        costs = [sm.get_cost()]

        for i in range(x, n):
            sm.remove(nums[i - x])
            sm.add(nums[i])

            costs.append(sm.get_cost())

        # Part 2: Dynamic Programming
        INF = float('inf')

        prev = [0] * (n + 1)

        for t in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):

                # Option 1: Skip current position
                curr[i] = curr[i - 1]

                # Option 2: Select a window of size x
                if i >= x:
                    start = i - x

                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[start]
                    )

            prev = curr

        return prev[n]

        