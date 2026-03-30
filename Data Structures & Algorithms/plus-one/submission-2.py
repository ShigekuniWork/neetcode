class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        count_up = True

        for i in range(len(digits) -1, -1, -1):
            if digits[i] + 1 == 10:
                digits[i] = 0
            else:
                digits[i] += 1
                count_up = False
                break
        
        if count_up:
            digits = [1] + digits
        
        return digits