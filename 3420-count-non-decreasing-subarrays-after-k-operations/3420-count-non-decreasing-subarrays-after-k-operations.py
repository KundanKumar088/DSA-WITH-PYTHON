
from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:

        n = len(nums)
        dq = deque()

        right = n - 1
        cost = 0
        ans = 0

        for i in range(n - 1, -1, -1):

            # Merge smaller segments
            while dq and nums[dq[-1]] < nums[i]:

                l = dq.pop()

                r = dq[-1] if dq else right + 1

                cost += (r - l) * (nums[i] - nums[l])

            dq.append(i)

            # Shrink window if cost exceeds k
            while cost > k:

                r = dq[0]

                cost -= nums[r] - nums[right]

                if r == right:
                    dq.popleft()

                right -= 1

            # Count valid subarrays
            ans += right - i + 1

        return ans
