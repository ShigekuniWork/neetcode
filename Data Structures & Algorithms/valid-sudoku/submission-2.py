class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                cur = board[row][col]
                if  cur == ".":
                    continue
                
                if (cur in rows[row] or
                    cur in cols[col] or
                    cur in squares[(row // 3, col // 3)]):
                    return False
                
                cols[col].add(cur)
                rows[row].add(cur)
                squares[(row//3, col//3)].add(board[row][col])
        
        return True