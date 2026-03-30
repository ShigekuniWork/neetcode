class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = [[] for _ in range(k)]
        min_heap = []
        for x, y in points:
            distance = x ** 2 + y ** 2
            min_heap.append([distance, x, y])
        
        heapq.heapify(min_heap)
        for i in range(k):
            _, x, y = heapq.heappop(min_heap)
            res[i] = [x, y]

        return res