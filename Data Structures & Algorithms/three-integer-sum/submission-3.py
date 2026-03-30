class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        I'd apprach this problem by using two pointer.
        First, I'll sorte nums so that prevent from duplication pairs.
        Second, Itrate though nums and calucurate total of current number
        and left pointer and right pointer. 
        If the total is 0, this total is the pair.
        If total is not pair, change pointer and serach pair.
        """

        # Assign empty list to 'response'
        response = []
        
        # Sort nums
        nums.sort()

        # Start loop, 'i' and 'cur' over the `nums` index and value
        for i, cur in enumerate(nums):
            if cur > 0:
                break
            
            if i > 0 and cur == nums[i - 1]:
                continue
            
            # Assign next index of current and last index to left, right
            left, right = i + 1, len(nums) - 1
            # Continue loop until left is grater than right
            while left < right:
                total = cur + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    response.append([cur, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return response
        """
        So This aproach use two loops for itrate nums and serach pair, Time complexity
        is O(n^2)
        
        Space complexity is O(1) or O(n) extra space depending on the sorting algorithm.
        O(m) spaces for the output list
        """