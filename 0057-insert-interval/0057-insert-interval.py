class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            end = result[-1]

            if end[1] >= intervals[i][0]:
                end[1] = max(end[1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result           


            
