class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n =len(nums)
        minend = nums[0]
        maxend = nums[0]
        ans = nums[0]

        for i in range(1,n):
            v1 =minend*nums[i]
            v2 = maxend*nums[i]
            v3 = nums[i]

            minend = min(v3,min(v1,v2))
            maxend = max(v3,max(v1,v2))

            ans = max(ans,maxend,minend)
        return ans    