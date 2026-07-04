class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []


        intervals.sort()
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            last_interval=result[-1]

            if last_interval[1] >= intervals[i][0]:
                last_interval[1] = max(last_interval[1] , intervals[i][1])

            else:
                result.append(intervals[i])    

        return result        

            