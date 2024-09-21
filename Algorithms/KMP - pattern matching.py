"""
Problem: Find the Index of the First Occurrence in a String
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # If the needle is empty, return 0
        if not needle:
            return 0
        
        # Create a lookup table for the needle
        lps = self.build_kmp_lookup(needle)
        
        # Pointers for the haystack and needle
        i = 0
        j = 0

        # Iterate through the haystack
        while i<len(haystack):

            # If the characters match, increment both the pointers
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            
            # If the characters don't match
            else:
                # If the needle pointer is at the start, increment the haystack pointer
                if j==0:
                    i+=1
                # Else, move the needle pointer back to the max length of the previous prefix suffix
                else:
                    j=lps[j-1]
            
            # If the needle pointer is at the end, return the index
            if j==len(needle):
                return i-j

        # If the needle is not found, return -1
        return -1
    
    def build_kmp_lookup(self,s):

        # Stores the max length of a prefix that is equal to a suffix for the string of     
        # length i
        lps = [0]*len(s)

        # How many previous characters have we matched, and are avoiding
        prev_lps = 0

        # Current pointer
        i=1

        while i<len(s):

            # If the character is matching, increment the previous char matched and store it
            # in the lps dp
            if s[prev_lps] == s[i]:
                lps[i] = prev_lps+1
                prev_lps+=1
                i+=1

            # If the characters don't match
            else:
                # If there are no characters to avoid, assign the length 0 and increment
                # the counter iterator
                if prev_lps == 0:
                    lps[i] = 0
                    i+=1
                # Move back by again checking for one character, and assign the prev_lps as
                # the max length of prefix suffix sum till that character
                else:
                    prev_lps = lps[prev_lps-1]

        # Return the lookup table
        return lps