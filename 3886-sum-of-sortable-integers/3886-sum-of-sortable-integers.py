class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:


        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True
            prev_max = float("-inf")

            for l in range(0, n, k):
                r = l + k
                block = nums[l:r]

                # Count circular descents
                descents = 0
                for i in range(k):
                    if block[i] > block[(i + 1) % k]:
                        descents += 1

                # A block must be sortable by rotation
                if descents > 1:
                    valid = False
                    break

                # Sorted blocks must join in non-decreasing order
                block_min = min(block)
                block_max = max(block)

                if prev_max > block_min:
                    valid = False
                    break

                prev_max = block_max

            if valid:
                ans += k

        return ans

        