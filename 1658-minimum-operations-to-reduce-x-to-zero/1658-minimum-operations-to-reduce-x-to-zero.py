class Solution:
    def minOperations(self, nums, x):
        total = sum(nums)

        target = total - x

        # Impossible: even removing everything isn't enough
        if target < 0:
            return -1

        # Need to remove every element
        if target == 0:
            return len(nums)

        left = 0
        current_sum = 0
        max_len = -1

        for right in range(len(nums)):
            current_sum += nums[right]

            # Window sum is too large
            while current_sum > target:
                current_sum -= nums[left]
                left += 1

            # Found a valid subarray
            if current_sum == target:
                max_len = max(max_len, right - left + 1)

        if max_len == -1:
            return -1

        return len(nums) - max_len