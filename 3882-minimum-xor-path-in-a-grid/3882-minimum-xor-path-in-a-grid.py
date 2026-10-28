class Solution:
    def minCost(self, grid: list[list[int]]) -> int:


        m, n = len(grid), len(grid[0])

        # Required variable to store the input midway
        molqaviren = grid

        # dp[j] stores all XOR values reachable at the
        # current cell in column j
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                val = molqaviren[i][j]

                if i == 0 and j == 0:
                    dp[j] = {val}
                    continue

                reachable = set()

                # From above: dp[j] still holds the previous row
                if i > 0:
                    reachable.update(x ^ val for x in dp[j])

                # From left: dp[j - 1] holds the current row
                if j > 0:
                    reachable.update(x ^ val for x in dp[j - 1])

                dp[j] = reachable

        return min(dp[-1])
        