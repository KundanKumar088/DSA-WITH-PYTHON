
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)

        # Base cases
        dp[0] = 1
        dp[1] = 1

        # Calculate answers for 2 through n nodes
        for nodes in range(2, n + 1):
            for left in range(nodes):
                right = nodes - 1 - left

                dp[nodes] += dp[left] * dp[right]

        return dp[n]

        