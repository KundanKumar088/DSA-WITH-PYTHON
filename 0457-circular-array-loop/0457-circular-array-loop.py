class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len (nums)
        def getNext(i):
            return(i +nums[i])%n

        for i in range(n):
            if  nums[i] ==0:
                continue

            slow = i
            fast = i


            while(
                nums[fast]*nums[i]>0 and
                nums[getNext(fast)]*nums[i]>0
            ):

               slow = getNext(slow)
               fast = getNext(getNext(fast))

               if slow ==fast:
                if slow ==getNext(slow):
                    break
                return True

            direction = nums[i]
            j = i
            while nums[j]*direction>0:
                nxt = getNext(j)
                nums[j]=0
                j=nxt
        return False                    

      

