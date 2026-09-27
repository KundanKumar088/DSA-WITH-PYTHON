class Solution:
    def isMatch(self, s, p):
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            first_match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == '.')
            )

            if j + 1 < len(p) and p[j + 1] == '*':
                result = (
                    dfs(i, j + 2) or
                    (first_match and dfs(i + 1, j))
                )
            else:
                result = first_match and dfs(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return dfs(0, 0)
        