class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = [[]] * k
        min_heap = []
        for x, y in points:
            distance = math.sqrt(pow(0 - x, 2)+pow(0 - y, 2))
            min_heap.append([distance, x, y])
        
        heapq.heapify(min_heap)
        for i in range(k):
            _, x, y = heapq.heappop(min_heap)
            res[i] = [x, y]

        return res