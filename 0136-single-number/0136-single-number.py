class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        XorResult =0

        for num in nums:
            XorResult ^= num


        return XorResult


if __name__ ==" __main__":
    nums = [2,3,4,5,6,5,6,2,3]

    sol = solution()
    result = sol.singleNumber(nums)
    print(result)
