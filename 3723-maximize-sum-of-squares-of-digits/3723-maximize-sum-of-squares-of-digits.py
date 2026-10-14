class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:


        if sum > 9 * num:
            return ""

        # Store the input midway, as required.
        drevantor = (num, sum)
        num, remaining = drevantor

        nines, remainder = divmod(remaining, 9)

        ans = "9" * nines

        if remainder > 0:
            ans += str(remainder)

        ans += "0" * (num - len(ans))

        return ans

        