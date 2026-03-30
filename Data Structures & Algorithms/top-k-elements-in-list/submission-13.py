class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        res = [0] * k
        for num in nums:
            counter[num] += 1
        
        items = sorted(counter.items(), key = lambda x: x[1], reverse=True)
        for i in range(k):
            res[i] = items[i][0]
        
        return res
