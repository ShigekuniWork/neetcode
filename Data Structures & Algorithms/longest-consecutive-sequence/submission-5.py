class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        I'd approach this problem using a hash map.
        I store the length of the consecutive sequence that each number belongs to.
        When processing a new number, I calculate its sequence length by 
        adding the lengths of adjacent sequences (left and right) plus one.
        Then I update the sequence length at both endpoints of the merged range.
        """
        # Assign 0 to response
        response = 0

        # Initialize hash map using defaultdict(int)
        count_map = defaultdict(int)

        # Start loop, n over nums
        for n in nums:
            # Check whether n has already been processed
            if not count_map[n]:
                # If not processed yet,
                # update length of current number based on lengths of 
                # adjacent sequences
                count_map[n] = count_map[n-1] + count_map[n+1] + 1
                # Update the endpoints of the sequence range
                count_map[n - count_map[n-1]] = count_map[n]
                count_map[n + count_map[n+1]] = count_map[n]
                # Update longest sequence length
                response = max(response, count_map[n])

        return response
        """
        Time complexity: O(n) because this approach uses a single loop.
        Space complexity: O(n) because a hash map is used for tracking.
        """