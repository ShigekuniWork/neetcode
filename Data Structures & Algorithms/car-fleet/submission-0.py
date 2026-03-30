class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 0:
            return 0

        cars = sorted(zip(position, speed), reverse=True)

        time_to_target = [(target - p) / s for p, s in cars]
        fleets = 1
        last_fleet_time = time_to_target[0]

        for t in time_to_target[1:]:
            if t > last_fleet_time:
                last_fleet_time = t
                fleets += 1
        
        return fleets

        
