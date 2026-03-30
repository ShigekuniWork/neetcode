class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, - 1, - 1):
            last = min(len(nums), nums[i] + i + 1)

            for j in range(i + 1, last):
                if dp[j]:
                    dp[i] = True
                    break
        
        return dp[0]