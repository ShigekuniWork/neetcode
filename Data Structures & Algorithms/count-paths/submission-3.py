class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n for _ in range(m)]

        for row in range(m-2,-1,-1):
            for col in range(n-2, -1, -1):
                grid[row][col] = grid[row][col + 1] + grid[row + 1][col]
        
        return grid[0][0]
