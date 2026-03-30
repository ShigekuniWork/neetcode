class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        num_rows = len(word1)
        num_cols = len(word2)
        
        grid = [[0] * (num_cols + 1) for _ in range(num_rows + 1)]

        for col in range(num_cols + 1):
            grid[num_rows][col] = num_cols - col

        for row in range(num_rows + 1):
            grid[row][num_cols] = num_rows - row

        for row in range(num_rows - 1, -1, -1):
            for col in range(num_cols - 1, -1, -1):
                
                down = grid[row + 1][col]
                right = grid[row][col + 1]
                diagonal = grid[row + 1][col + 1]

                if word1[row] == word2[col]:
                    grid[row][col] = diagonal
                else:
                    grid[row][col] = 1 + min(down, right, diagonal)
                    
        return grid[0][0]