class Solution:
    def countBits(self, n: int) -> List[int]:
        response = [0] * (n + 1)

        for i in range(n + 1):
            response[i] = response[i >> 1] + (i & 1)

        return response