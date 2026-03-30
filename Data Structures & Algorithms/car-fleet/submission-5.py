class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: 
        cars = sorted(zip(position, speed), reverse = True)

        res = 1
        current = (target - cars[0][0]) / cars[0][1]
        for i in range(1, len(position)):
            time = (target - cars[i][0]) / cars[i][1]
            if time > current:
                current = time
                res += 1

        return res