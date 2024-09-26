"""
1. Learned to sort a dictionary by its values
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter

        counts = { c:val for c,val in sorted(Counter(s).items(),key=lambda x: x[1],reverse=True)}

        keys = list(counts.keys())
        curr = 0
        
        if counts[keys[0]] > math.ceil(len(s)/2):
            return ''

        ans = ['']*len(s)

        for i in range(0,len(s),2):
            ans[i] = keys[curr]
            counts[keys[curr]]-=1
            if counts[keys[curr]] == 0:
                curr+=1
            
        for i in range(1,len(s),2):
            ans[i] = keys[curr]
            counts[keys[curr]]-=1
            if counts[keys[curr]] == 0:
                curr+=1

        return ''.join(ans)