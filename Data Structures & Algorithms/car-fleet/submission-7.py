class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: 
        cars = sorted(zip(position, speed), reverse = True)
        stack = []

        for p, s in cars:
            current = (target - p) / s
            if stack and stack[-1] >= current:
                continue
            stack.append(current)
        
        return len(stack)
                