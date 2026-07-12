class Solution(object):
   def merge(self, arr, low, mid, high):
       n1 = mid - low + 1
       n2 = high - mid
       left = arr[low:mid + 1]
       right = arr[mid + 1:high + 1]
      
       i, j, k = 0, 0, low
       while i < n1 and j < n2:
           if left[i] <= right[j]:
               arr[k] = left[i]
               i += 1
           else:
               arr[k] = right[j]
               j += 1
           k += 1
      
       while i < n1:
           arr[k] = left[i]
           i += 1
           k += 1
      
       while j < n2:
           arr[k] = right[j]
           j += 1
           k += 1
  
   def countPairs(self, arr, low, mid, high):
       right = mid + 1
       count = 0
       for i in range(low, mid + 1):
           while right <= high and arr[i] > 2 * arr[right]:
               right += 1
           count += (right - (mid + 1))
       return count
  
   def mergeSort(self, nums, low, high):
       count = 0
       if low < high:
           mid = (low + high) // 2
           count += self.mergeSort(nums, low, mid)
           count += self.mergeSort(nums, mid + 1, high)
           count += self.countPairs(nums, low, mid, high)
           self.merge(nums, low, mid, high)
       return count
  
   def reversePairs(self, nums):
       low = 0
       high = len(nums) - 1
       return self.mergeSort(nums, low, high)



        