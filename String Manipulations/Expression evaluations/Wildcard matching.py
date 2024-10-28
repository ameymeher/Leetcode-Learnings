from functools import cache


"""
1. The edge / base cases are very important
2. What should happen when either pattern is empty or the text is empty
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        new_p = []
        
        for i in range(len(p)):
            if new_p and p[i] == new_p[-1] == '*':
                continue
            new_p.append(p[i])

        p = ''.join(new_p)

        @cache
        def check(s_pointer,p_pointer):
            nonlocal s,p

            if s_pointer == len(s) and p_pointer == len(p):
                return True

            if p_pointer >= len(p):
                return False

            if s_pointer >= len(s):
                if p[p_pointer] == '*':
                    return check(s_pointer,p_pointer+1)
                else:
                    return False

            if p[p_pointer] == '*':
                return (check(s_pointer,p_pointer+1) 
                        or check(s_pointer+1,p_pointer))
            
            if p[p_pointer] in {s[s_pointer],'?'}:
                return check(s_pointer+1,p_pointer+1)
            
            return False

        return check(0,0)