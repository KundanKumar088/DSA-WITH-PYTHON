class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)

        if n<2:
            return 0

        mn = min(nums)
        mx = max(nums)

        if mn == mx:
            return 0

        bucket_size = (mx - mn + n -2)// (n-1)

        bucket_count = (mx-mn)// bucket_size + 1

        bucket_min = [float('inf')] * bucket_count
        bucket_max = [float('-inf')] * bucket_count


        for num in nums:
            idx = (num-mn)// bucket_size

            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)

        ans = 0
        prev_max = mn

        for i in range(bucket_count):
            if bucket_min[i] == float('inf'):
                continue

            ans = max(ans, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]

        return ans                    