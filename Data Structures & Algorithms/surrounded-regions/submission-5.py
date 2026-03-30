class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        q = deque()

        for r in range(rows):
            for c in (0, cols - 1):
                if board[r][c] == "O":
                    board[r][c] = "#" 
                    q.append((r, c))
        
        for c in range(cols):
            for r in (0, rows - 1):
                if board[r][c] == "O":
                    board[r][c] = "#"
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "#"
                    q.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
