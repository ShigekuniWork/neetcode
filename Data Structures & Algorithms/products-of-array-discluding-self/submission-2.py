class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = 1, 1
        response = [1] * len(nums)

        # prefix
        for i in range(len(nums)):
            response[i] *= prefix
            prefix *= nums[i]

        # suffix
        for i in range(len(nums)-1, -1, -1):
            response[i] *= suffix
            suffix *= nums[i]

        return response