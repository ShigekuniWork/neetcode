class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        I would approach this problem by using two-pointer technique.
        First, I sort the list to make it easy to handle duplicates.
        Then, for each number, use two pointers to find the other two numbers that
        sum up to zero
        """
        # First, sort the array so that duplicate elements can be skkiped easliy
        # and two-pointer movement is predictable.
        nums.sort()

        # Initialize response to store valid triplets
        response = []

        # Iterate through array with both index 'i' and value 'cur'
        for i, cur in enumerate(nums):
            # If the currenet value is greter than zero, stop the loop
            # because all remaining numbers are positive and cannot the sum zero.
            if cur > 0:
                break
            
            # Skip the number that it is the same as previous one to avoid duplicat results
            if i > 0 and cur == nums[i-1]:
                continue
            
            # set up two-pointer
            # left stats after 'i'
            left = i + 1
            # 'right' stats from the end.
            right = len(nums) -1

            # Continue while 'left' is less than 'right'
            while left < right:
                # Calucurate total
                total = cur + nums[left] + nums[right]

                # If the total is less than zero, move 'right' one step left to decrease the sum
                if total > 0:
                    right -= 1
                # If the total is greater than zerom 'left' one step right to increase to the sum
                elif total < 0:
                    left += 1
                # When the total equals zero, a valid triplet is found
                else:
                    response.append([cur, nums[left], nums[right]])
                    # Move both pointers inward after storing the result.
                    left += 1
                    right -= 1

                    # Skip duplicate elements for the the 'left' pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                
            
        return response


