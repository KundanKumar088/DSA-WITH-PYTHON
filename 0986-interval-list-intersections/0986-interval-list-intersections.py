class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n = len(firstList)
        m = len(secondList)
        

        i = 0
        j = 0
        result = []

        while i<n and j<m:
            start1 , end1 = firstList[i]
            start2 , end2 = secondList[j]

            start = max(start1, start2)
            end  = min(end1 , end2)

            if start<=end:
                result.append([start, end])

            if end<end2:
                i  +=1
            else:
                j +=1
        return result             
        

