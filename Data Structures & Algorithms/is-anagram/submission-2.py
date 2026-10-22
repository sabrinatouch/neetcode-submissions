class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Take input s and t
        # Evaluate: if s and t are anagrams of each other
        # If the s and t ARE anagrams of each other
            # return True
        # Else if the s and t ARE NOT anagrams of each other
            # return False

        ## Test cases
        # 1. Test true
        # input: s = 'dog', t = 'god'
        # output: True

        # one of the strings doesn't have to be a real word?
        # input: s = 'cat', t = 'tca'
        # output: True

        # multiple same letters
        # input: s = 'bottom' t = 'ttoobm'
        # output: True

        # valid anagram even with one letter
        # input: s = 'x', t = 'x'
        # output: True

        # 2. Test false
        # input: s = 'bottom' t = 'tobm'
        # output: False

        # input: s = 'cat' t = 'cam'
        # output: False

        # input: s = null, t = null
        # output: False

        # input: s = 'race', t = 'racecar'
        # output: False?

        ## Clarifying questions
        # - could a string be null?
        # - could a string have a mix of capital and lowercase letters
        # - Could there be non-alphabet characters in the string? Whitespace?
        # strings >= 1

        ## Pseudo solution
        # If s and t are not the same length
        # Therefore s and t aren't anagrams
            # return False

        # s='dog', t='god'
        # dict =
            # d, 0
            # o, 0
            # g, 0
        # t =
            # g
            # o
            # d

        # s='cat', t='tam'
        # dict =
            # c, 1
            # a, 0
            # t, 0
        # t =
            # t
            # a
            # m

        # (key, value) pairs 
        # Put one of the strings into a dictionary
            # ('r', 2)
        # Start at the beginning of the string t
            # Check if char t is in the dict of unmatched chars
            # If char t does exist in the dict
            # That means there's match (corresponding character in both strings)
                # decrease the value of the match character in the dict by -1 to signify that that char has been used to find a match
                # then we can look at the next char in string t
            # If char t does not exist in dict
                # return False
        # If we've looked at all chars in t
        # and the dict is empty
            # return True
        # (If dictionary is not empty)
            # (return False)

        ## Implementation
        dict_unmatched_chars = {}

        for char in s:
            if char in dict_unmatched_chars:
                dict_unmatched_chars[char] += 1
            else:
                dict_unmatched_chars[char] = 1
        
        for char in t:
            if char in dict_unmatched_chars:
                dict_unmatched_chars[char] -= 1
                if dict_unmatched_chars[char] == 0:
                    del dict_unmatched_chars[char]
            elif char not in dict_unmatched_chars:
                return False

        if dict_unmatched_chars == {}:
            return True
        elif dict_unmatched_chars != {}:
            return False
        

        
            