"""
Learnings:
1. No need to compare for all of the strings
2. Compare only the minimum and maximum strings
3. Decreases the time complexity
"""

"""
Assumptions:

1. Array of strings only, can there be no elements? No
2. Not sorted according to the lengths of the strings
3. array is given in the function
4. Return the length of the prefix? No the prefix

prefix = []

Edge case:
1. "abc","abd"
"""

def get_longest_common_prefix(arr):

    prefix = [] # O(min_length) space
    min_length = min(arr,key=len) #O(N) time
    
    for i in range(min_length): # O(min_lenth) time
        prefix.append(arr[0][i])
        for word in arr:        # O(N) time
            if word[i] != prefix[-1]:
                prefix.pop()
                break

    
    return ''.join(prefix)

"""
prefix = ['a','b']

Time complexity: O(N*min_length)
Space complexity: O(N)
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_str = min(strs)
        max_str = max(strs)

        res = ''

        for i in range(min(len(min_str),len(max_str))):
            if min_str[i] == max_str[i]:
                res += min_str[i]
            else:
                break
                    
        return res

"""
A better solution with O(N+min_length) time complexity
space : O(1)
"""