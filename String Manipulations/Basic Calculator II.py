"""
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5

1. For evaluating the expression, + and - are evaluated later, * and / are evaluated first.
2. Need to check if the last operator was * or /, then do the operation and store the value in a last_val variable.
3. If the last operator was + or -, then add the last_val to the result. Set the last_val appropriately (For -, negate and set).
4. At the end, add the last_val to the result.
"""

# Method 1:
class Solution:
    def calculate(self, s: str) -> int:
        
        op = '+'
        curr_val = 0
        last_val = 0
        res = 0

        for i,c in enumerate(s):
            if c.isdigit():
                curr_val*=10
                curr_val+=int(c)

            # Need an if here because we need to do the operation if its the last character
            if not c.isdigit() or i==len(s)-1:
                
                # Skip the operations if " ", but just perform if its the last character
                if c==" " and i!=len(s)-1:
                    continue
                if op == "+":
                    res += last_val
                    last_val = curr_val
                elif op == "-":
                    res+= last_val
                    last_val = -curr_val
                elif op == "*":
                    last_val = last_val * curr_val
                elif op == '/':
                    # Need to truncate towards zero. // and math.floor truncates towards - infinity. 
                    #last_val = math.trunc(last_val / curr_val) 
                    last_val = int(last_val / curr_val)

                curr_val = 0
                op = c

        res += last_val
        return res