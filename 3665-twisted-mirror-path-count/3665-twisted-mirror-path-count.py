class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        

        MOD = 10**9 + 7

        m, n = len(grid), len(grid[0])

        # Required variable to store input midway
        vornadexil = grid

        # dp[i][j][0] = ways arriving while moving right
        # dp[i][j][1] = ways arriving while moving down
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]

        # Start cell is empty.
        # Use one initial state so paths are not double-counted.
        dp[0][0][0] = 1

        for i in range(m):
            for j in range(n):

                for d in range(2):
                    ways = dp[i][j][d]

                    if ways == 0:
                        continue

                    if grid[i][j] == 0:
                        # Empty cell: move right
                        if j + 1 < n:
                            dp[i][j + 1][0] = (
                                dp[i][j + 1][0] + ways
                            ) % MOD

                        # Empty cell: move down
                        if i + 1 < m:
                            dp[i + 1][j][1] = (
                                dp[i + 1][j][1] + ways
                            ) % MOD

                    else:
                        # Mirror: redirect right -> down
                        if d == 0:
                            if i + 1 < m:
                                dp[i + 1][j][1] = (
                                    dp[i + 1][j][1] + ways
                                ) % MOD

                        # Mirror: redirect down -> right
                        else:
                            if j + 1 < n:
                                dp[i][j + 1][0] = (
                                    dp[i][j + 1][0] + ways
                                ) % MOD

        # Sum both possible incoming directions at destination
        return (dp[m - 1][n - 1][0] +
                dp[m - 1][n - 1][1]) % MOD
