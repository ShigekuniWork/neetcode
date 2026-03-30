class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = dr + r, dc + c
                if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited:
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)

        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols -1, atlantic)

        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows-1, c, atlantic)

        return list(pacific & atlantic)