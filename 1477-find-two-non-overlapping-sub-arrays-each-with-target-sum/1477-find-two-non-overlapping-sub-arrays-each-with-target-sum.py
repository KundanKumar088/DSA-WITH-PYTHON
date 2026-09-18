class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        # best[i] = minimum length of a valid subarray
        # ending at or before index i
        best = [float('inf')] * n

        prefix = 0
        mp = {0: -1}

        ans = float('inf')
        min_len = float('inf')

        for i in range(n):
            prefix += arr[i]

            if prefix - target in mp:
                j = mp[prefix - target]

                # Current subarray = arr[j+1 ... i]
                length = i - j

                # Previous subarray can end at index j
                if best[j] != float('inf'):
                    ans = min(ans, length + best[j])

                min_len = min(min_len, length)

            best[i] = min_len

            mp[prefix] = i

        return -1 if ans == float('inf') else ans
        