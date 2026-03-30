class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])

        start, end = intervals[0]
        overlap = 0
        for i in range(1, len(intervals)):
            if end > intervals[i][0]:
                end = min(end, intervals[i][1])
                overlap += 1
            else:
                end = intervals[i][1]

        return overlap