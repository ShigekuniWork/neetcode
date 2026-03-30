class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # val -> index

        for i, v in enumerate(nums):
            compair = target - v
            if compair in seen:
                return [seen[compair], i]
            
            seen[v] = i
        
        return []