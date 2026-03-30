class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[-1]
        curr = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if curr < 0:
                curr = 0
            curr += nums[i]
            res = max(res, curr)
        
        return res