class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
    
        n = len(bloomDay)

        # Not enough flowers
        if m * k > n:
            return -1

        left = min(bloomDay)
        right = max(bloomDay)
        answer = -1

        while left <= right:
            days = (left + right) // 2

            bouquets = 0
            flowers = 0

            for day in bloomDay:

                if day <= days:
                    # Flower has bloomed
                    flowers += 1

                    # k adjacent flowers make one bouquet
                    if flowers == k:
                        bouquets += 1
                        flowers = 0

                else:
                    # Flower has not bloomed
                    # Adjacent sequence breaks
                    flowers = 0

            if bouquets >= m:
                # This number of days works.
                # Try fewer days.
                answer = days
                right = days - 1

            else:
                # Not enough bouquets.
                # Need more days.
                left = days + 1

        return answer