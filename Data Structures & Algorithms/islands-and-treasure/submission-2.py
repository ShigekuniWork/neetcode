class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        treasure = 2147483647

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))
        
        while queue:
            row, col = queue.popleft()

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc
            
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == treasure:
                    grid[nr][nc] = grid[row][col] + 1
                    queue.append((nr, nc))