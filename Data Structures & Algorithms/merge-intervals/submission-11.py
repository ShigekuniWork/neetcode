class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]

        for interval in intervals[1:]:
            start, end = interval[0], interval[1]
            last_end = res[-1][1]

            if last_end < start:
                res.append(interval)
            else:
                res[-1][1] = max(end, last_end)
        
        return res