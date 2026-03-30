class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1, dp2 = 0, 0

        for n in nums:
            temp = dp1
            dp1 = max(dp1, dp2)
            dp2 = temp + n

        return max(dp1, dp2)