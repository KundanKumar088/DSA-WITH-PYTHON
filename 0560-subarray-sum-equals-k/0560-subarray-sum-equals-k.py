class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)


        pre_sum = 0
        ans = 0
        m = {0: 1}  # Initial prefix sum = 0 with 1 occurrence


        for i in range(n):
           pre_sum += nums[i]
          
           # Check if (pre_sum - k) is present in the map
           if pre_sum - k in m:
               ans += m[pre_sum - k]
          
           # Store prefix sum frequency
           m[pre_sum] = m.get(pre_sum, 0) + 1
      
        return ans

        