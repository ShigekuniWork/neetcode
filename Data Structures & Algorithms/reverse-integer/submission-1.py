class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = (1 << 31) - 1  # 2147483647
        INT_MIN = -(1 << 31)     # -2147483648

        reversed_value = 0
        
        # 反転処理を行うための、x の絶対値コピー
        remaining_digits = abs(x) 
        
        while remaining_digits != 0:
            if reversed_value > INT_MAX // 10:
                return 0

            current_digit = remaining_digits % 10
            remaining_digits //= 10 

            reversed_value = reversed_value * 10 + current_digit
            
        if x < 0:
            reversed_value *= -1

        if reversed_value < INT_MIN or reversed_value > INT_MAX:
            return 0
             
        return reversed_value