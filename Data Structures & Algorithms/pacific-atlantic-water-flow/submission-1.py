class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()
        dirs = ((1,0),(-1,0),(0,1),(0,-1))

        def dfs(r: int, c: int, seen: set):
            seen.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen:
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, seen)

        for c in range(n):
            dfs(0, c, pac)
            dfs(m - 1, c, atl)
        for r in range(m):
            dfs(r, 0, pac)
            dfs(r, n - 1, atl)

        return list(pac & atl)
