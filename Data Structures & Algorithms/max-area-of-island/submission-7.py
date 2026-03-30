class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        q = deque()
        rows = len(grid)
        cols = len(grid[0])

        def bfs(q):
            res = 1

            while q:
                row, col = q.popleft()
                for dr, dc in [(0, 1), (0, -1),(1, 0), (-1, 0)]:
                    nr, nc = dr + row, dc + col
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 0
                        res += 1

            return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append((r, c))
                    grid[r][c] = 0
                    res = max(res, bfs(q))

        return res