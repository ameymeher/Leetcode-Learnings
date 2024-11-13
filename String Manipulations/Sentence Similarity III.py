"""
You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be separated from existing words by spaces.

For example,

s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in s1.
s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although there is a sentence "s are" inserted into s1, it is not separated from "Frog" by a space.
Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.

1. Idiotically tried to find a contiguous length which can be removed
2. Better way was to see that if the smaller sentence can be formed by the max prefix and max suffix, we can get the answer.
3. Since the smaller sentence can be created by either the front, or the back or both, but won't be created by any part in the middle.
4. Keep an eye out on the indexes, that's where you do most of the mistakes
"""


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        s_arr = sentence1.split()
        l_arr = sentence2.split()

        if len(s_arr) > len(l_arr):
            s_arr,l_arr = l_arr,s_arr

        max_prefix_length = 0
        for i in range(len(s_arr)):
            if s_arr[i] == l_arr[i]:
                max_prefix_length+=1
            else:
                break

        max_suffix_length = 0
        for i in range(len(s_arr)):
            if s_arr[len(s_arr)-1-i] == l_arr[len(l_arr)-1-i]:
                max_suffix_length+=1
            else:
                break

        if max_prefix_length + max_suffix_length >= len(s_arr):
            return True

        return False