"""
1. Slicing operation is very expensive, try to pass indexes instead of slicing. Its O(n) expensive

"""

# Without slicing
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        @cache
        def palindrome_check(l,r,k):
            nonlocal s
            
            if l >= r:
                return True

            if s[l] == s[r]:
                return palindrome_check(l+1,r-1,k)

            if s[l]!= s[r]:
                if k==0:
                    return False
                return (palindrome_check(l+1,r,k-1) or 
                        palindrome_check(l,r-1,k-1))

        return palindrome_check(0,len(s)-1,k)
    

# With slicing
class Solution:
    @cache
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        if s == "" or len(s) == 1 or len(set(s)) == 1:
            return True

        l = 0
        r = len(s)-1

        while l<=r:
            if s[l] != s[r]:
                if k == 0:
                    return False
                return (self.isValidPalindrome(s[l:r],k-1) 
                        or self.isValidPalindrome(s[l+1:r+1],k-1))

            l+=1
            r-=1
        
        return True