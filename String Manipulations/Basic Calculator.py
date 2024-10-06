"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

1. Reversing the string and using a stack to solve this problem.
2. If the character is a digit, then keep adding it to the curr_num. Remember to reverse the string.
3. If the character is an operator, then check if the curr_num is not None, then add it to the stack.
4. If the character is a ")", then add it to the stack.
5. If the character is a "+", then add the curr_num to the stack.
6. If the character is a "-", then add the curr_num to the stack and negate the last element in the stack.
7. If the character is a "(", then add the curr_num to the stack and calculate the total of the elements in the stack until ")" is found.
8. At the end, add the curr_num to the stack and return the sum of the elements in the stack.
"""


class Solution:
    def calculate(self, s: str) -> int:
        
        s = s[::-1]
        stack = []

        curr_num = None

        for c in s:

            if c.isdigit():
                if curr_num is None:
                    curr_num = ''
                curr_num+=c
            else:
                if c == ' ' and curr_num is not None:
                    stack.append(int(curr_num[::-1]))
                    curr_num = None

                if c == ')':
                    if curr_num is not None:
                        stack.append(int(curr_num[::-1]))
                    stack.append(c)
                    curr_num = None
                    continue

                elif c == '+':
                    if curr_num is not None:
                        stack.append(int(str(curr_num)[::-1]))
                    curr_num = None

                elif c == '-':
                    if curr_num is not None:
                        stack.append(int(curr_num[::-1]))
                    stack[-1] *= -1
                    curr_num = None

                elif c == '(':
                    if curr_num is not None:
                        stack.append(int(curr_num[::-1]))

                    total = 0
                    while stack[-1] !=')':
                        total += stack.pop()
                    stack.pop()
                    stack.append(total)

                    curr_num = None

        ans = 0

        if curr_num:
            ans = int(curr_num[::-1])

        while stack:
            ans+=stack.pop()

        return ans