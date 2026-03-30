class Solution:
    def minMeetingRooms(self, intervals):
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        rooms = end_i = 0

        print(starts)
        for s in starts:
            if s < ends[end_i]:
                rooms += 1
            else:
                end_i += 1
        return rooms
