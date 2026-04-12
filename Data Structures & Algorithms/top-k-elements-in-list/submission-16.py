class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build a frequency map that counts how many times each number appers.
        count = {}
        # Create a list of groups `freq`, where freq[i] will store all numbsers that appear exactly i times
        freq = [[] for _ in range(len(nums) + 1)]

        # For each number and its freqency in the map, add the number to freq[cnt]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        # Initialize empty result list
        res = []
        for i in range(len(freq) -1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res