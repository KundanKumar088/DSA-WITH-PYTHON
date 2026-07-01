class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        repeated = -1

        # Find repeated number
        for row in grid:
            for num in row:
                if num in seen:
                    repeated = num
                seen.add(num)

        # Find missing number
        missing = -1
        for num in range(1, n * n + 1):
            if num not in seen:
                missing = num
                break

        return [repeated, missing]               