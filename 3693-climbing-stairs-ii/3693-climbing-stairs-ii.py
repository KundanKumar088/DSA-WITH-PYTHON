
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        dp = [float('inf')] * (n + 1)

        # Starting position
        dp[0] = 0

        # Calculate minimum cost for every step
        for i in range(1, n + 1):

            # Jump from previous 1, 2, or 3 steps
            for jump in range(1, 4):

                prev = i - jump

                if prev >= 0:
                    current_cost = (
                        dp[prev]
                        + costs[i - 1]
                        + jump * jump
                    )

                    dp[i] = min(dp[i], current_cost)

        return dp[n]

        