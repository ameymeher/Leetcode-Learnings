"""
Problem definition:
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        from functools import reduce
        from bisect import bisect_left

        wordDict = set(wordDict)
        possible_indexes = [-1]

        # Only check for the previous max_length length as that is only available in the wordDict
        max_length = reduce(lambda x,y: max(x,len(y)),wordDict,0)

        for i in range(len(s)):

            # Get the start indexes
            start_indexes = possible_indexes[bisect_left(possible_indexes,i-max_length):]

            # Just check for these start indexes if a substring is possible
            for start in start_indexes:
                if s[start+1:i+1] in wordDict:
                    possible_indexes.append(i)
                    break
            
        # If the possible indexes has the last index, then it is possible
        return True if possible_indexes[-1] == len(s)-1 else False