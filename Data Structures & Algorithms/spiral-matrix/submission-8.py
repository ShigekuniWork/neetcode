class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        directions = [
            (0, 1), # right
            (1, 0), # down
            (0, -1), # left
            (-1, 0), # up
        ]

        steps = [len(matrix[0]), len(matrix) - 1]
        row, col, d = 0, -1, 0
        while steps[d&1]:
            for i in range(steps[d&1]):
                row += directions[d][0]
                col += directions[d][1]
                res.append(matrix[row][col])
            steps[d&1] -= 1
            d += 1
            d %= 4

        return res
