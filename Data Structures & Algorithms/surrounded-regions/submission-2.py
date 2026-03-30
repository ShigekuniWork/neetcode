class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(row, col):
            if not (row in range(rows) and col in range(cols) and board[row][col] == "O"):
                return
            
            board[row][col] = "#"
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                dfs(dr + row, dc + col)
        
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][-1] == "O":
                dfs(r, cols -1)
        
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[-1][c] == "O":
                dfs(rows-1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"