"""
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

1. XOR gives 0 for the same element twice
2. Can be used to see if there are even or odd number of elements
3. If the XOR is 0, then the number of vowels are even
4. If the XOR is same, then the number of vowels are even
5. In this problem, we have to store all the invalid states of XOR in a hashmap
6. If we have observed the invalid state before, then we know that if we remove the elements till the previous state, we can get the longest substring
7. If we have not observed the invalid state before, then we store the current state in the hashmap
"""

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """
        1. vowels, even number of times
        2. Longest substring
        3. All are lowercase letters

        s = "leetminicowor"

        e:2
        i:2
        o:2
        """
        prev_xor = 0
        ans = 0
        prev_xor_map = {}

        for i,c in enumerate(s):
            if c in set(['a','e','i','o','u']):
                prev_xor^=ord(c)
            
            if prev_xor == 0:
                ans = max(ans,i) + 1
            else:
                if prev_xor in prev_xor_map:
                    ans = max(ans, i - (prev_xor_map[prev_xor]))
                else:
                    prev_xor_map[prev_xor] = i

        return ans

"""

"eleetminicoworoep"

prev_xor = 0 ^ 2 ^ 2 ^ 2
prev_xor_map = {
    2:0
}
i=3
ans = 3
"""