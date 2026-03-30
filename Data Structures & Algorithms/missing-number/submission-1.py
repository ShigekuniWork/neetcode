class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expect = len(nums)
        actual = 0

        for i in range(len(nums)):
            expect += i
            actual += nums[i]
        
        return expect - actual
        