class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        size = m+n
        index= size-1
        i=m-1
        j=n-1


        while i>=0 and j>=0:
            if nums1[i] <=nums2[j]:
                nums1[index] =nums2[j]
                j -=1

            else:
                nums1[index] = nums1[i]
                i -=1
            index -=1

        while j>=0:
            nums1[index] =nums2[j]
            j -=1
            index -=1


if __name__== "__main__":

    nums1=[1,2,3,0,0,0]
    m=3
    nums2=[2,5,6]
    n=3

    sol=Solution()
    sol.merge(nums1,m,nums2,n)

    print(nums1)



