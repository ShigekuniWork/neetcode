class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        response = right

        while left <= right:
            k = (left + right) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                response = k
                right = k - 1
            else:
                left = k + 1
        
        return response