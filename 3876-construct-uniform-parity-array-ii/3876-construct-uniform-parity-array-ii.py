class Solution:
    def uniformArray(self, nums1):
        mn = min(nums1)

        # If the minimum is odd,
        # we can make every element odd.
        if mn % 2 == 1:
            return True

        # Minimum is even.
        # Then every element must be even.
        for x in nums1:
            if x % 2 == 1:
                return False

        return True
        