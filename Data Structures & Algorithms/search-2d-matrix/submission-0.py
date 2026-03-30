class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rowLength = len(matrix)
        colLength = len(matrix[0])

        left = 0
        right = (rowLength * colLength) - 1

        while left <= right:
            mid = left + (right - left) // 2

            midRow, midCol = divmod(mid, colLength)
            val = matrix[midRow][midCol]

            if target > val:
                left = mid + 1
            elif target < val:
                right = mid - 1
            else:
                return True
        
        return False