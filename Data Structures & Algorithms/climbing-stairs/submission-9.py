class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 1, 1
        
        for _ in range(n):
            temp = curr
            curr += prev
            prev = temp

        return prev