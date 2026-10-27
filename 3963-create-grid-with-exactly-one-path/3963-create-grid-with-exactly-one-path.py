class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:


        grid = [['#'] * n for _ in range(m)]

        # Open every cell in the first row
        grid[0] = ['.'] * n

        # Open every cell in the last column
        for i in range(m):
            grid[i][n - 1] = '.'

        return [''.join(row) for row in grid]
        