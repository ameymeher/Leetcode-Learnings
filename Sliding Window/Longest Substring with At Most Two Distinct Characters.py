class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        from collections import defaultdict

        win_counts = defaultdict(int) #{b:1,a:1}
        l = 0 #3
        max_length = 0 #3
        
        # Increment the r value
        for r in range(len(s)): #4

            # Inculcate the r pointer value
            win_counts[s[r]] += 1

            # Slide the l to check for a valid window
            while l<=r and len(win_counts) > 2:
                win_counts[s[l]]-=1
                if win_counts[s[l]] == 0:
                    del win_counts[s[l]]
                l+=1

            # Update the ans
            max_length = max(max_length,r-l+1)

        return max_length