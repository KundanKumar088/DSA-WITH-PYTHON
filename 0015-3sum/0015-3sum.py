class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        
        

       result = []
       nums.sort() 
       n = len(nums)


    
       for i in range(n - 2):
           if i > 0 and nums[i] == nums[i - 1]: 
               continue


           target = -nums[i]
           left, right = i + 1, n - 1


           #  Two-pointer approach
           while left < right:
               sum_val = nums[left] + nums[right]


               if sum_val == target:
                   result.append([nums[i], nums[left], nums[right]])


                   #  Skip duplicate values
                   while left < right and nums[left] == nums[left + 1]:
                       left += 1
                   while left < right and nums[right] == nums[right - 1]:
                       right -= 1


                   left += 1
                   right -= 1
               elif sum_val < target:
                   left += 1
               else:
                   right -= 1


       return result


# Main test
# if __name__ == "__main__":
#    sol = Solution()
#    nums = [-1, 0, 1, 2, -1, -4]
#    res = sol.threeSum(nums)
#    for triplet in res:
#        print(triplet)

