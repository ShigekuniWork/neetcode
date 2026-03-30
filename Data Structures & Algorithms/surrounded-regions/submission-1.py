class Solution:
    PROTECTED_O = '#' 

    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return

        num_rows, num_cols = len(board), len(board[0])

        def mark_connected_os(row_index, col_index):
            if (row_index < 0 or row_index >= num_rows or
                col_index < 0 or col_index >= num_cols or
                board[row_index][col_index] != 'O'):
                return

            board[row_index][col_index] = self.PROTECTED_O
            
            mark_connected_os(row_index + 1, col_index) 
            mark_connected_os(row_index - 1, col_index) 
            mark_connected_os(row_index, col_index + 1) 
            mark_connected_os(row_index, col_index - 1) 

        for col_index in range(num_cols):
            if board[0][col_index] == 'O':
                mark_connected_os(0, col_index)
            if board[num_rows - 1][col_index] == 'O':
                mark_connected_os(num_rows - 1, col_index)

        for row_index in range(num_rows):
            if board[row_index][0] == 'O':
                mark_connected_os(row_index, 0)
            if board[row_index][num_cols - 1] == 'O':
                mark_connected_os(row_index, num_cols - 1)

        for row_index in range(num_rows):
            for col_index in range(num_cols):
                if board[row_index][col_index] == 'O':
                    # 保護されずに残っている 'O' は、完全に囲まれていることを意味するため、
                    # 問題の要件に従って 'X' に反転する
                    board[row_index][col_index] = 'X'
                elif board[row_index][col_index] == self.PROTECTED_O:
                    # '#' にマークされたマスは、境界線と繋がっていた 'O' なので、元の 'O' に戻す
                    board[row_index][col_index] = 'O'
                    