class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        I'd apprach this problem by iterating outside and inside loops.
        First, Itarate outside and inside over the nums index.
        Then I calcurate diffrence btween outside num and inside num against 0
        check wether the diffrence number in the nums after outside index.
        """
        nums.sort()

        # Assign empty list to the valiable response
        response = []

        # Iterate outside and inside loop over nums
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # Calucurate diffrence, the results assign to diffrence
                diffrence = -1 * (nums[i] + nums[j])
                # Check wether the diffrence be in nums
                if diffrence in nums[j+1:] and [nums[i], nums[j], diffrence] not in response:
                    # If the condition True Append the tree pair
                    response.append([nums[i], nums[j], diffrence])

        return response

        """
        This apprach is O(n^2) time complecity, because Itration done outside and inside
        Space complecity is O(N), this is needed to ansewer this problem  
        """