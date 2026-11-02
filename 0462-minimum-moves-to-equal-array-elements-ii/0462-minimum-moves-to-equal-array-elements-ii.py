class Solution:
    def minMoves2(self, nums: list[int]) -> int:


        nums.sort()

        # Find the median
        median = nums[len(nums) // 2]

        # Calculate total moves
        moves = 0
        for num in nums:
            moves += abs(num - median)

        return moves
        