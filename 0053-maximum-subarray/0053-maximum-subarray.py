class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        bestend = nums[0]
        ans = nums[0]

        for i in range(1, n):
            v1 = bestend+nums[i]
            v2 = nums[i]

            bestend = max(v1,v2)
            ans = max(bestend, ans)

        return ans