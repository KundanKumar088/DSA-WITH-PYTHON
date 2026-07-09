class Solution:
    def trap(self, height: List[int]) -> int:
       n = len(height)


       ans = 0
       lmax = height[0]  # Maximum height on the left
       rmax = height[n - 1]  # Maximum height on the right
       low = 1  # Pointer from the left
       high = n - 2  # Pointer from the right


       while low <= high:
           lmax = max(lmax, height[low])
           rmax = max(rmax, height[high])


           if lmax < rmax:
               ans += lmax - height[low]
               low += 1
           else:
               ans += rmax - height[high]
               high -= 1


       return ans