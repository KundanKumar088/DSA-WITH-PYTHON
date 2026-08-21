class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)


        while left < right:
            mid = (left + right)//2

            subarray = 1
            curr_sum = 0

            for num in nums:
                if curr_sum + num > mid:
                    subarray +=1
                    curr_sum = num
                else:
                    curr_sum += num

            if subarray <= k:
                right = mid
            else:
                left = mid+1

        return left                        