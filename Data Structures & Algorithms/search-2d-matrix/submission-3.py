class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        colLen = len(matrix)
        rowLen = len(matrix[0])

        left = 0
        right = colLen * rowLen - 1
        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, rowLen)
            cur = matrix[row][col]

            if cur < target:
                left = mid + 1
            elif cur > target:
                right = mid - 1
            else:
                return True
        
        return False