class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:

        ans = [0] * k

        # dp[r] = number of subarrays ending at previous position
        # whose product % k == r
        dp = [0] * k

        for num in nums:

            # New DP for subarrays ending at current position
            newDp = [0] * k

            # Only remainder matters
            numMod = num % k

            # Start a new subarray containing only num
            newDp[numMod] += 1

            # Extend all previous subarrays
            for r in range(k):

                newRemainder = (r * numMod) % k

                newDp[newRemainder] += dp[r]

            # Add current subarrays to final answer
            for r in range(k):
                ans[r] += newDp[r]

            # Move to next position
            dp = newDp

        return ans
        