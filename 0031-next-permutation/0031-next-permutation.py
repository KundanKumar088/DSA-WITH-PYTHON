class Solution:
   def swap(self, nums, i, j):
       nums[i], nums[j] = nums[j], nums[i]


   def reverse(self, nums, start, end):
       while start < end:
           self.swap(nums, start, end)
           start += 1
           end -= 1


   def nextPermutation(self, nums):
       """
       :type nums: List[int]
       :rtype: None. Do not return anything, modify nums in-place instead.
       """
       n = len(nums)
       index = -1


       # Step 1: Find the first decreasing element from the right
       for i in range(n - 2, -1, -1):
           if nums[i] < nums[i + 1]:
               index = i
               break


       # Step 2: Find the next greater element to swap with nums[index]
       if index != -1:  # If such an element is found
           for i in range(n - 1, index, -1):
               if nums[i] > nums[index]:
                   self.swap(nums, i, index)
                   break


       # Step 3: Reverse the suffix (right part of the array)
       self.reverse(nums, index + 1, n - 1)




      



        