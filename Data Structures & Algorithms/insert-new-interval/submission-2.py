class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        s, e = newInterval
        it = iter(intervals)

        for a, b in it:
            if e < a:
                res.append([s, e])
                res.append([a, b])
                res.extend(it)
                return res
            elif s > b:
                res.append([a, b])
            else:
                s = min(s, a)
                e = max(e, b)

        res.append([s, e])
        return res
