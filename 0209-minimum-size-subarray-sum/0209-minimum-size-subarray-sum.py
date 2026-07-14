class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        high=0
        low= 0
        curr_sum = 0
        min_len = float('inf')
         
        for high in range(n):
            curr_sum +=nums[high]

            while curr_sum>=target:
                min_len =min(min_len,high-low+1)
                curr_sum -=nums[low]
                low +=1

        return 0 if min_len ==float('inf') else min_len



            
            


             