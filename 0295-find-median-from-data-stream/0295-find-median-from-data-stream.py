
import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # Max heap (store negative values)
        self.large = []  # Min heap

    def addNum(self, num: int) -> None:
        # Add to the larger half first
        heapq.heappush(self.large, num)

        # Move the smallest element of large to small
        heapq.heappush(self.small, -heapq.heappop(self.large))

        # Keep large equal in size to small or one larger
        if len(self.small) > len(self.large):
            heapq.heappush(
                self.large, -heapq.heappop(self.small)
            )

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return float(self.large[0])

        return (-self.small[0] + self.large[0]) / 2.0

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()