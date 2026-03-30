class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols):
                return 0
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0
    
            return (1 + dfs(r + 1, c) +
                        dfs(r -1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c -1))

        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))
        
        return area