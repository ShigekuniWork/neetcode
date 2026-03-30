class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_min, cur_max = 1, 1

        for num in nums:
            product_max = num * cur_max
            product_min = num * cur_min

            cur_max = max(product_max, product_min, num)
            cur_min = min(product_max, product_min, num)
            res = max(res, cur_max)

        return res


