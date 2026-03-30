class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_max, cur_min = 1, 1

        for num in nums:
            old_max = cur_max * num
            cur_max = max(old_max, cur_min * num, num)
            cur_min = min(old_max, cur_min * num, num)

            res = max(res, cur_max)
        
        return res