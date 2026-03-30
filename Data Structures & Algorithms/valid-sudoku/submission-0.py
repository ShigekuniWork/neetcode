class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Setの代わりに、整数のリストを9つ用意する
        rows_mask = [0] * 9  
        cols_mask = [0] * 9
        squares_mask = [[0] * 3 for _ in range(3)] 

        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                if cur == ".":
                    continue
                
                n = int(cur) 
                
                flag = 1 << n 

                if (rows_mask[r] & flag) or \
                (cols_mask[c] & flag) or \
                (squares_mask[r // 3][c // 3] & flag):
                    return False

                rows_mask[r] |= flag
                cols_mask[c] |= flag
                squares_mask[r // 3][c // 3] |= flag

        return True