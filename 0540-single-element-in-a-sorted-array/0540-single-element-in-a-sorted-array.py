class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            # Make mid even
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                # Pair is correct, single element is to the right
                low = mid + 2
            else:
                # Pair is broken, single element is at mid or left
                high = mid

        return nums[low]              




            
               
