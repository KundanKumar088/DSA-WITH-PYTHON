class Solution(object):
   def productExceptSelf(self, nums):
       """
       :type nums: List[int]
       :rtype: List[int]
       """
       n = len(nums)
      
       # Create answer array and initialize with 1
       ans = [1] * n


       # Calculate prefix product and store in ans
       for i in range(1, n):
           ans[i] = ans[i - 1] * nums[i - 1]


       # Calculate suffix product and update ans
       suffix = nums[n - 1]
       for i in range(n - 2, -1, -1):
           ans[i] = ans[i] * suffix  # prefix * suffix
           suffix *= nums[i]


       return ans
