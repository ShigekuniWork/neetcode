class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        write_index = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[write_index][1]:
                intervals[write_index][1] = max(intervals[write_index][1], intervals[i][1])
            else:
                write_index += 1
                intervals[write_index] = intervals[i]
        
        return intervals[:write_index + 1]