class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_end =0
        min_end = 0
        max_sum = 0
        min_sum = 0

        for num in nums:
            max_end = max(num, max_end + num)
            max_sum = max(max_sum, max_end)

            min_end = min(num, min_end + num)
            min_sum = min(min_sum, min_end)

        return max(max_sum, -min_sum)