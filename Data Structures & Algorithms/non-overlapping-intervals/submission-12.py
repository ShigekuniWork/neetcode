class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prev_end = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if prev_end > start:
                res += 1
            else:
                prev_end = end
        
        return res