class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = (1 << 32) - 1
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a < (1 << 31) else a - (1 << 32)

