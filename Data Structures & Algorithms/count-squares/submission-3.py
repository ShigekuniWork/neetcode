class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        total = 0
        target_x, target_y = point

        for (x, y), freq in self.points.items():
            dx, dy = abs(x - target_x), abs(y - target_y)
            if dx != dy or dx == 0:
                continue
            
            total += (
                freq * self.points.get((x, target_y), 0) * self.points.get((target_x, y), 0))
        
        return total