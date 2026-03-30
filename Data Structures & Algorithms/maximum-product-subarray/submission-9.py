class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_min = curr_max = 1

        for num in nums:
            calc_max = curr_max * num
            calc_min = curr_min * num

            curr_max = max(calc_max, calc_min, num)
            curr_min = min(calc_max, calc_min, num)

            res = max(res, curr_max)

        return res