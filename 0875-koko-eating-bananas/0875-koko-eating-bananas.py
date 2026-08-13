class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            guess = (left + right) // 2

            hours = 0
            for pile in piles:
                hours += (pile + guess - 1) // guess

            if hours <= h:
                right = guess
            else:
                left = guess + 1

        return left               