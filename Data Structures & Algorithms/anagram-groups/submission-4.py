class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        I'd aproach this problem by using hash map.
        First, Iterate thought strs, then sort the value.
        Second, I check wether the soted value in the hash map.
        If it is in hash map, I append it hash map values
        Therd, I conver hash map values to list to return output. 
        """

        # Assign defautdict(list) to the hash_map to write simple code.
        hash_map = defaultdict(list)

        # Start loop, s over strs
        for s in strs:
            # Sort s in order to serach values form hash_map
            sorted_s = ''.join(sorted(s))
            # Append original s to hash_map values
            hash_map[sorted_s].append(s)
        
        # Convert hash_map values to the output, then retunr the resulst
        return list(hash_map.values())