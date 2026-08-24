class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap =[]

        for num in arr:
            heapq.heappush(heap,(-abs(num-x) ,  -num))

            if len(heap)> k:
                heapq.heappop(heap)

                
        return sorted([-num for _, num in heap])           