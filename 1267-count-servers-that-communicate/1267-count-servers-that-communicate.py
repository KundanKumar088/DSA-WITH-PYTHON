
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row_count = [0] * m
        col_count = [0] * n

        # First pass: Count servers in rows and columns
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        # Second pass: Count communicating servers
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        ans += 1

        return ans

        