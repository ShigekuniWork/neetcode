class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0
        rowLen = len(grid)
        colLen = len(grid[0])

        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directions = ((0,1), (0,-1), (1,0), (-1, 0))
        while fresh > 0 and q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(rowLen) and col in range(colLen) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            
            time += 1
        return time if fresh == 0 else -1