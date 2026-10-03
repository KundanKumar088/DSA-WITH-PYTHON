class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False

        width = valueDiff + 1
        buckets = {}

        for i, x in enumerate(nums):

            # Remove element outside the sliding window
            if i > indexDiff:
                old = nums[i - indexDiff - 1]
                old_bucket = old // width
                del buckets[old_bucket]

            bucket = x // width

            # Same bucket
            if bucket in buckets:
                return True

            # Previous bucket
            if bucket - 1 in buckets:
                if abs(x - buckets[bucket - 1]) <= valueDiff:
                    return True

            # Next bucket
            if bucket + 1 in buckets:
                if abs(x - buckets[bucket + 1]) <= valueDiff:
                    return True

            buckets[bucket] = x

        return False  