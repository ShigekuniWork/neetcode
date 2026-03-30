class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(arr: List[int]) -> int:
            rob1, rob2 = 0, 0
            for num in arr:
                rob1, rob2 = rob2, max(rob1+num, rob2)
            
            return rob2
        

        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))
        
