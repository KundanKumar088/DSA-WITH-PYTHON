class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        freq = {0:1}

        for num in nums:
            prefix += num
            rem =prefix % k

            if rem < 0:
                rem +=k

            count +=freq.get(rem, 0)
            freq[rem] = freq.get(rem, 0) +1
        return count         
        



              



         
         


        