import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = Counter(nums)

        for num , count in freq.items():
            heapq.heappush(heap,(count, num))

            if len(heap)>k:
                heapq.heappop(heap)

        return[num for count, num in heap]       
        