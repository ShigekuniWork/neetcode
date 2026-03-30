class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        response = []
        nums.sort()

        def dfs(i:int, cur: List[int], total: int) -> None:
            if total == target:
                response.append(cur.copy())
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()
        dfs(0, [], 0)
        return response