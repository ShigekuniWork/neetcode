class Solution:

    def encode(self, strs: List[str]) -> str:
        response = ""

        for c in strs:
            word_length = len(c)
            response += str(word_length) + "#" + c

        return response

    def decode(self, s: str) -> List[str]:
        response = []
        left = 0
        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
            word_length = int(s[left:right])
            left = right + 1
            right = left + word_length
            response.append(s[left:right])
            left = right
    
        return response