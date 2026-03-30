class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
            px, py = point
            res = 0

            # キーを回すのは正しい (O(N)のため)
            for x, y in list(self.ptsCount.keys()):
                dx, dy = x - px, y - py
                
                # 正方形の条件: |dx| == |dy| かつ 辺の長さ > 0
                if abs(dx) != abs(dy) or dx == 0:
                    continue
                
                # 残りの2点の座標を定義 (CとD)
                point_C = (px, y)  # (px, y)
                point_D = (x, py)  # (x, py)
                
                # 点B(x, y)、点C、点Dの存在数を確認し、全て掛け合わせる
                res += self.ptsCount[(x, y)] * self.ptsCount[point_C] * self.ptsCount[point_D]
                
            return res
