class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(row, col, idx):
            if idx == len(word):
                return True
            if not (0 <= row < rows and 0 <= col < cols):
                return False
            if word[idx] != board[row][col] or board[row][col] == "#":
                return False

            board[row][col] = "#"
            res = (dfs(row + 1, col, idx + 1) or
                dfs(row - 1, col, idx + 1) or
                dfs(row, col + 1, idx + 1) or
                dfs(row, col - 1, idx + 1))
            board[row][col] = word[idx]
        
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False