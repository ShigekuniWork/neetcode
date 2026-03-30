from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        response = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            response[sorted_s].append(s)
        
        return list(response.values())