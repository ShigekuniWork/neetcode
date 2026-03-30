class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        res = [0] * (rows * cols)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = [cols, rows -1]

        row, col, d = 0, -1, 0
        res_index = 0
        while steps[d & 1]:
            for i in range(steps[d & 1]):
                row += directions[d][0]
                col += directions[d][1]
                res[res_index] = matrix[row][col]
                res_index += 1
            steps[d & 1] -= 1
            d = (d + 1) % 4

        return res