

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0

        for x in arr1:
            idx = bisect_left(arr2, x - d)

            if idx == len(arr2) or arr2[idx] > x + d:
                count += 1

        return count

        