"""
Solution 1: Brute Force
"""
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        l,r = 0, len(s)-1
        pal_r = len(s)-1

        while l<=r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                if l==0:
                    r-=1
                l=0
                pal_r = r
            
        print(s[:pal_r])

        return ''
    
"""
Solution 2: Using two pointers and taking advantage of a constraint
"""
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        l = 0
        
        if not s:
            return s

        for r in range(len(s)-1,-1,-1):
            if s[l] == s[r]:
                l+=1
        
        if l == len(s):
            return s

        return (
                    ''.join(reversed(s[l:])) + 
                    self.shortestPalindrome(s[:l]) +
                    s[l:]
        )

"""
Solution 3: Using KMP
"""

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        kmp_s = s + '#' + s[::-1]

        # A dp array suggesting the maximum length of prefix = suffix for the string of length i
        def build_kmp_lookup(s):

            lookup = [0]*len(s)

            prev_lps = 0
            i = 1
            
            while i<len(s):
                if s[i] == s[prev_lps]:
                    lookup[i] = prev_lps+1
                    prev_lps+=1
                    i+=1
                else:
                    if prev_lps == 0:
                        lookup[i] = 0
                        i+=1
                    else:
                        prev_lps = lookup[prev_lps-1]

            return lookup


        lookup = build_kmp_lookup(kmp_s)

        return (
            ''.join(reversed(s[lookup[-1]:])) + s
        )