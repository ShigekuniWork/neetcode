class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        I'd approach to solve this problem by using # tags and recording each word length.
        Iterate through the strs, then set a # tag for marking the start of the word.
        Then get the current word length and add it to the response.
        Set a # tag after the word length to mark the end of the length.
        Set the current word after the # tag.

        For Example: #4#word#4#code
        """
        # Assign empty value to 'response'
        response = ""

        # Loop start, s over strs:
        for s in strs:
            # Get word length
            s_length = len(s)
            # Set described value to response
            response += '#' + str(s_length) + '#' + s
        
        return response

    def decode(self, s: str) -> List[str]:
        """
        I'd approach to decode the string by using two pointers to slice the string.
        First, search for the first # from the string, then move the right pointer forward to the next #.
        Second, get the word length by using two pointers and extract the word.
        Then repeat for the other words as well.
        """
        # Initialize left pointer and response
        left = 0
        response = []
        
        # Iterate while left pointer is less than the string length
        while left < len(s):
            # Search second #
            right = left + 1
            while s[right] != '#':
                right += 1
            # Extract word length
            word_length = int(s[left+1:right])
            end_of_word = right + word_length
            # Extract word by using extracted length
            word = s[right + 1: end_of_word+1]
            # Then append it to the response
            response.append(word)
            # Move left to end_of_word + 1
            left = end_of_word + 1 

        return response