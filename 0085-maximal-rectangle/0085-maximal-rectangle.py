class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * (cols + 1)
        ans = 0

        for row in matrix:
            # Build histogram
            for j in range(cols):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Monotonic increasing stack
            stack = [-1]

            for j in range(cols + 1):
                while stack[-1] != -1 and heights[stack[-1]] > heights[j]:
                    h = heights[stack.pop()]
                    width = j - stack[-1] - 1
                    ans = max(ans, h * width)

                stack.append(j)

        return ans