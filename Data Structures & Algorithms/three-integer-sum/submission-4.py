class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        I'd approach this problem by using the two-pointer technique.
        First, sort the array to make it easier to handle duplicates.
        Then, for each number, use two pointers to find the other two numbers
        that sum up to zero.
        """

        # First, sort the array so that duplicate elements can be skipped easily
        # and the two-pointer movement becomes predictable.
        nums.sort()

        # Prepare an empty list to store triplets whose sum is zero.
        response = []

        # Iterate through the array with both index 'i' and value 'cur'.
        for i, cur in enumerate(nums):
            # If the current number is greater than zero, stop the loop,
            # because all remaining numbers are positive and cannot make the sum zero.
            if cur > 0:
                break

            # Skip this number if it is the same as the previous one to avoid duplicate results.
            if i > 0 and cur == nums[i - 1]:
                continue

            # Set up two pointers: 'left' starts after 'i', 'right' starts from the end.
            left, right = i + 1, len(nums) - 1

            # Continue while 'left' is less than 'right'.
            while left < right:
                total = cur + nums[left] + nums[right]

                # If the total is greater than zero, move 'right' one step left to decrease the sum.
                if total > 0:
                    right -= 1

                # If the total is less than zero, move 'left' one step right to increase the sum.
                elif total < 0:
                    left += 1

                # When the total equals zero, a valid triplet is found.
                else:
                    response.append([cur, nums[left], nums[right]])

                    # Move both pointers inward after storing the result.
                    left += 1
                    right -= 1

                    # Skip duplicate elements for the 'left' pointer.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        # Return all unique triplets that sum to zero.
        return response

        """
        The time complexity is O(n squared) because for each number,
        a two-pointer scan goes through the rest of the array linearly,
        and sorting doesn’t dominate that cost.
        The space complexity is constant because the algorithm only uses
        a few pointers and modifies the array in place without extra data structures.
        """
