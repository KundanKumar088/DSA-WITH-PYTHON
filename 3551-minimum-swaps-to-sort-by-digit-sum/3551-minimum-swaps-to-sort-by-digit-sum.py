class Solution:
    def minSwaps(self, nums: List[int]) -> int:


        def digit_sum(x):
            total = 0
            while x > 0:
                total += x % 10
                x //= 10
            return total

        n = len(nums)

        # Sort by digit sum, then by number
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Map each number to its target index
        pos = {num: i for i, num in enumerate(sorted_nums)}

        visited = [False] * n
        swaps = 0

        # Count permutation cycles
        for i in range(n):
            if visited[i]:
                continue

            j = i
            cycle_size = 0

            while not visited[j]:
                visited[j] = True
                cycle_size += 1
                j = pos[nums[j]]

            swaps += cycle_size - 1

        return swaps
        