"""
1. This was naturally not a sliding window problem, as shifting the l was confusing
2. A tweak in the problem made this a sliding window problem
"""

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        from collections import Counter, defaultdict

        counts = Counter(s)
        flag = True

        for val in counts.values():
            if val < k:
                flag = False
                break

        if flag:
            return len(s)

        def slide_window_for_n_unique(n):
            nonlocal s,k
     
            l = 0
            win_counts = defaultdict(int)
            max_length = 0

            for r in range(len(s)):
                
                win_counts[s[r]]+=1

                while l<=r and len(win_counts)>n:
                    win_counts[s[l]]-=1
                    if win_counts[s[l]] == 0:
                        del win_counts[s[l]]
                    l+=1
                
                valid = True
                for v in win_counts.values():
                    if v < k:
                        valid = False
                        break

                if valid:
                    max_length = max(max_length,r-l+1)

            return max_length

        ans = 0
        for i in range(len(counts)+1):
            ans = max(ans,slide_window_for_n_unique(i))

        return ans