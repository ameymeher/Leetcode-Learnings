"""
Perform the following shift operations on a string:

Right shift: Replace every letter with the successive letter of the English alphabet, where 'z' is replaced by 'a'. For example, "abc" can be right-shifted to "bcd" or "xyz" can be right-shifted to "yza".
Left shift: Replace every letter with the preceding letter of the English alphabet, where 'a' is replaced by 'z'. For example, "bcd" can be left-shifted to "abc" or "yza" can be left-shifted to "xyz".
We can keep shifting the string in both directions to form an endless shifting sequence.

For example, shift "abc" to form the sequence: ... <-> "abc" <-> "bcd" <-> ... <-> "xyz" <-> "yza" <-> .... <-> "zab" <-> "abc" <-> ...
You are given an array of strings strings, group together all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:

Input: strings = ["a"]

Output: [["a"]]

1. Make a note about the modulus operator behavior in python.
2. a%b gives the result with the same sign as b.
3. If b is negative, then the result will be negative.
4. If b is positive, then the result will be positive.
5. -1%26 = 25
"""

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        from collections import defaultdict

        diff_map = defaultdict(list)

        for word in strings:
            if len(word) == 1:
                diff_map[(-1)].append(word)
            else:
                diff_arr = []
                for i in range(1,len(word)):
                    diff = (ord(word[i]) - ord(word[i-1]))%26
                    diff_arr.append(diff)
                diff_arr = tuple(diff_arr)
                diff_map[diff_arr].append(word)

        return list(diff_map.values())