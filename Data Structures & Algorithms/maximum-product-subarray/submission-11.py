class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_num = max_num = 1
        res = nums[0]

        for n in nums:
            calc_max_num = max_num * n
            calc_min_num = min_num * n

            max_num = max(calc_max_num, calc_min_num, n)
            min_num = min(calc_max_num, calc_min_num, n)
            
            res = max(res, max_num)
        
        return res
