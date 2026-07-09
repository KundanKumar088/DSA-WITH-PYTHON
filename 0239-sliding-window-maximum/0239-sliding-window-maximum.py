class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       n = len(nums)
       result = []
       dq = deque()
      
       # Process first k elements
       dq.append(0)
       for i in range(1, k):
           while dq and nums[i] >= nums[dq[-1]]:
               dq.pop()
           dq.append(i)
      
       result.append(nums[dq[0]])
      
       # Process remaining elements
       for i in range(k, n):
           # Remove elements out of window
           if i - dq[0] >= k:
               dq.popleft()
          
           # Remove smaller elements
           while dq and nums[i] >= nums[dq[-1]]:
               dq.pop()
          
           dq.append(i)
           result.append(nums[dq[0]])
      
       return result
        