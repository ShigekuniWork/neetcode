def adjust_matches(
    char: str, 
    window_counts: Dict[str, int], 
    target_counts: Dict[str, int], 
    matches: int, 
    delta: int
) -> int:
    """ window_counts を delta 分更新し、matches を調整する """
    
    if char not in target_counts:
        return matches

    if window_counts.get(char, 0) == target_counts[char]:
        matches -= 1

    window_counts[char] += delta

    if window_counts[char] == target_counts[char]:
        matches += 1

    return matches

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        target_counts = Counter(s1)
        window_counts = Counter()
        matches = 0

        for i in range(len_s1):
            matches = adjust_matches(s2[i], window_counts, target_counts, matches, delta=+1)
        
        if matches == len(target_counts):
            return True

        for i in range(len_s1, len_s2):
            
            right_char = s2[i]
            matches = adjust_matches(right_char, window_counts, target_counts, matches, delta=+1)

            left_char = s2[i - len_s1]
            matches = adjust_matches(left_char, window_counts, target_counts, matches, delta=-1)
            
            if matches == len(target_counts):
                return True
        
        return False