class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_count = len(points)
        min_heap = [0] * points_count

        for i in range(points_count):
            x, y = points[i]
            dist = (x ** 2) + (y ** 2)
            min_heap[i] = (dist, x, y)
        
        heapq.heapify(min_heap)
        res = []
        while k > 0:
            _, x, y = heapq.heappop(min_heap)
            res.append([x, y])
            k -= 1
        
        return res