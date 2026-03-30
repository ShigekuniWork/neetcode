class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry_up = True
        for i in range(len(digits)-1, -1, -1):
            if not carry_up:
                break
            digits[i] += 1
            if digits[i] < 10:
                carry_up = False
            else:
                digits[i] = 0
        
        if carry_up:
            digits = [1] + digits
        
        return digits