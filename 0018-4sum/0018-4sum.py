class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
       nums.sort()
       unique_quad = set()
       n=len(nums)


       for i in range(n-3):
            for j in range(i+1 , n-2):
                val = target-nums[i]-nums[j]
                low,high =j+1 , n-1

                while low < high:
                    total = nums[low] + nums[high]
                    if total ==val:
                        unique_quad.add((nums[i] , nums[j] , nums[low], nums[high]))
                        low +=1
                        high-=1
                    elif total<val:
                        low +=1
                    else:
                        high -=1

       
       return [list(quad) for quad in unique_quad]           


if __name__ == "__main__":
    sol = Solution()
    nums = [1,0,-1,0,-2,2] 
    target = 0
    result = sol.fourSum(nums , target)
    for quad in result:
        print(quad)
    
