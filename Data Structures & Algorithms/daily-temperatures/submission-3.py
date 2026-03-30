class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for cur in range(n - 2, -1, -1):
            future = cur + 1

            while future < n and temperatures[future] <= temperatures[cur]:
                if temperatures[future] == 0:
                    future = n
                    break
                future += 1
            if future < n:
                res[cur] = future - cur

        return res