class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements_counter = defaultdict(int)
        for n in nums:
            elements_counter[n] += 1
        
        heap = []
        for value, count in elements_counter.items():
            heapq.heappush(heap,(count, value))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = [0] * k
        for i in range(k):
            res[i] = heapq.heappop(heap)[1]
        return res 

