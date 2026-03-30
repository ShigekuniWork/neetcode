class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        I'd approach to solve this problem by using two pointer.
        I assign first index and last index to left, right.
        Itrate though the heights list to compare left pointer and right pointer.
        Then I move either less one to next pinter and compare the result to ever maximum result. 
        """
        # Assign first index and last index to left, right
        left = 0
        right = len(heights) -1

        # Assign 0 to result
        result = 0

        # Loop starts while left index less than right index
        while left < right:
            # Calcurate current maximum amount of water
            amount = min(heights[left], heights[right]) * (right - left)

            # Compare current amount to even result
            result = max(result, amount)

            # Less one is maxmimum height currently
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return result
        """
        Time complexity is O(n) because this approach uses single loop only.
        Space complexity is O(1)
        """
