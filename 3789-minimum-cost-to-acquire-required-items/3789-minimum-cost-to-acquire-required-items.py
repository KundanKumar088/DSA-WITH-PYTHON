
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        mn = min(need1, need2)
        mx = max(need1, need2)

        # Case 1: Buy individual items
        cost_a = need1 * cost1 + need2 * cost2

        # Case 2: Buy combined items for common needs
        # and individual items for remaining needs
        cost_b = (
            mn * costBoth
            + (need1 - mn) * cost1
            + (need2 - mn) * cost2
        )

        # Case 3: Buy only combined items
        cost_c = mx * costBoth

        return min(cost_a, cost_b, cost_c)

        