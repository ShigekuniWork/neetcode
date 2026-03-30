class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(n: int) -> int:
            output = 0

            while n:
                degit = n % 10
                output += degit ** 2
                n = n // 10
            
            return output
        
        slow, fast = n, sum_of_squares(n)
        power = lam = 1

        while slow != fast:
            if power == lam:
                slow = fast
                power *= 2
                lam = 0
            fast = sum_of_squares(fast)
            lam += 1
        return True if fast == 1 else False
