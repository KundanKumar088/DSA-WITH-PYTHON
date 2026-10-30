
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # Convert integers into strings
        nums = list(map(str, nums))

        # Custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0

        # Sort using custom comparison
        nums.sort(key=cmp_to_key(compare))

        # Handle leading zeros
        if nums[0] == "0":
            return "0"

        # Join all numbers
        return "".join(nums)
             