"""
You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.

 

Example 1:

Input: s = "][]["
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".


1. There is a thing you need to deduce first.
2. The maximum number of balanced strings you can create with one swap is 2. Ex: ]][[ -> [][].
3. Therefore, find the number of unbalanced pairs first
4. Then, divide it by 2 and do a ceiling operation to get the number of swaps required.
"""

class Solution:
    def minSwaps(self, s: str) -> int:
        mismatches = 0
        for c in s:
            if c == ']' and mismatches != 0:
                mismatches-=1
            elif c == '[':
                mismatches+=1

        return math.ceil(mismatches/2)