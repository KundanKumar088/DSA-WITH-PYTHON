class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = left + (right - left)//2

            #target found
            if nums[mid] == target:
                return True

            #duplicates cannot determine which half is sorted
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            #left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1


            #right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1

        return False                                    