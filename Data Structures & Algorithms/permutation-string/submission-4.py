class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False

        s1_counts = [0] * 26
        window_counts = [0] * 26
        
        BASE_ORD = ord('a')

        for i in range(len_s1):
            s1_counts[ord(s1[i]) - BASE_ORD] += 1
            window_counts[ord(s2[i]) - BASE_ORD] += 1
        
        if s1_counts == window_counts:
            return True

        for i in range(len_s1, len_s2):
            window_counts[ord(s2[i]) - BASE_ORD] += 1
            window_counts[ord(s2[i - len_s1]) - BASE_ORD] -= 1

            if s1_counts == window_counts:
                return True

        return False