class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()

        for index, num in enumerate(nums):
            diff = target - num
            if diff in cache:
                return [cache[diff], index]
            cache[num] = index
        
        return []
        