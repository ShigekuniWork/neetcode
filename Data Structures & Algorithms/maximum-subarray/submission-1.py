class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = curr_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sub = max(max_sub, curr_sum)
        
        return max_sub