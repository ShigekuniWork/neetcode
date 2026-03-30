class Solution:
    def canJump(self, nums):
        far = 0

        for i, x in enumerate(nums):
            if far < i:
                return False
            far = max(far, i + x)
            if far >= len(nums) - 1:
                return True

        return False
