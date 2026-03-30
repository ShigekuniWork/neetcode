class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [1] * n

        for _ in range(m-2, -1, -1):
            for i in range(n-2, -1, -1):
                grid[i] += grid[i + 1]
            
        return grid[0]
