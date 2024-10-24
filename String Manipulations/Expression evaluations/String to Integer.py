"""
1. There are two conditions for overflow check, 
    if it is the same as INT_MAX//10, then the last digit should be checked
    if it is greater than INT_MAX//10, then it is overflow
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()

        if not s:
            return 0

        val = None
        negate = False
        INT_MAX = pow(2,31)-1
        INT_MIN = -pow(2,31)

        for c in s:
            if not c.isdigit():
                if val is None:
                    if c == '-':
                        negate = True
                        val = 0
                    elif c == '+':
                        val = 0
                    else:
                        return 0
                else:
                    return -val if negate else val
            else:
                if val is None:
                    val = 0

                if not negate and (val > INT_MAX//10 or (val == INT_MAX//10 and INT_MAX % 10 < int(c))):
                        return INT_MAX

                if negate and (val > -INT_MIN//10 or (val == -INT_MIN//10 and -(INT_MIN %-10) < int(c))): 
                    return INT_MIN

                if val == 0 and c=='0':
                    continue

                val*=10
                val+=int(c)

        return -val if negate else val