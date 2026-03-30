class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def dfs(row, col):
            nonlocal rows, cols
            if not (0 <= row < rows and 0 <= col < cols):
                return
            
            if grid[row][col] == "1":
                grid[row][col] = "#"
            else:
                return
            
            for dr, dc in [(0,1), (0,-1), (1, 0), (-1, 0)]:
                dfs(dr + row, dc + col)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)

        return res