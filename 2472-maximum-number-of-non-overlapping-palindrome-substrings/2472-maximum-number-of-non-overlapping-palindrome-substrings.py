class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Build palindrome table
        for i in range(n - 1, -1, -1):
            for j in range(i, n):

                if s[i] == s[j]:
                    if j - i <= 1:
                        pal[i][j] = True
                    else:
                        pal[i][j] = pal[i + 1][j - 1]

        # dp[i] = maximum number of non-overlapping
        # valid palindromes using first i characters
        dp = [0] * (n + 1)

        for i in range(n):
            
            # Don't choose a palindrome ending at i
            dp[i + 1] = dp[i]

            # Try every substring ending at i
            for j in range(i + 1):
                
                length = i - j + 1

                if length >= k and pal[j][i]:
                    dp[i + 1] = max(
                        dp[i + 1],
                        dp[j] + 1
                    )

        return dp[n]