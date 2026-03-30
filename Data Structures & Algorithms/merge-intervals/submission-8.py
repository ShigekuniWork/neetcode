class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
    
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            last_end = res[-1][1]

            if len(res) >= 1 and last_end >= start:
                res[-1][1] = max(last_end, end)
            else:
                res.append([start, end])

        return res