class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for s in strs:
            wordLength = len(s)
            res += str(wordLength) + "#" +s
        
        return res


    def decode(self, s: str) -> List[str]:
        left = 0
        right = 0
        res = []

        while left < len(s):
            while s[right] != "#":
                right += 1
            length = int(s[left:right])
            left = right + 1
            right = left + length
            word = s[left:right]

            res.append(word)
            left = right
        
        return res