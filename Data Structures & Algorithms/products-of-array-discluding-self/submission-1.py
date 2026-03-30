class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        I'd approach to solve this problem by using prefix and suffix.
        Iterate through nums and product nums and prefix that it is off by one
        current value of nums to expect current number, then append it to the response.
        Then Iterate through reversed list as well, suffix product to the response. 
        """
        # Assign one to the list value
        response = [1] * len(nums)

        # Loop start, i over index of nums
        prefix = 1
        for i in range(len(nums)):
            # Product prefix to response
            response[i] *= prefix
            # Update prefix as the result of product prefix and num
            prefix *= nums[i]

        # suffix loop start as well from end to first
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            response[i] *= suffix
            suffix *= nums[i]
        
        # return list that products of array except self
        return response

        """
        Time complexity is O(N)
        Space complexity is O(1)
        """