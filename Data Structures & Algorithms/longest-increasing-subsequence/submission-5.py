import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            target_index = bisect.bisect_left(tails, num)

            if target_index == len(tails):
                tails.append(num)
            else:
                tails[target_index] = num

        return len(tails)