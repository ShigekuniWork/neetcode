class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        prev_index = 0
        index = 0

        for i in range(len(nums)):
            index = prev_index if i>= 1 and nums[i] == nums[i - 1] else 0
            prev_index = len(res)
            for j in range(index, prev_index):
                curr = res[j].copy()
                curr.append(nums[i])
                res.append(curr)
        
        return res