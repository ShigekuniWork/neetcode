class Solution:
    def rob(self, nums: List[int]) -> int:
        case1, case2 = 0, 0
        for n in nums:
            case1, case2 = case2, max(n + case1, case2)
        
        return max(case1, case2)