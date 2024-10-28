class Solution:

    """
    1. s can be "" but p can be "a*". handle this case
    2. When the first character matches, then only move it plus 1 for the * case

    """
    def isMatch(self, s: str, p: str) -> bool:
        
        s_pointer = 0
        p_pointer = 0

        @cache
        def check(s_pointer,p_pointer):
            nonlocal s,p

            if s_pointer == len(s) and p_pointer == len(p):
                return True

            if p_pointer >= len(p):
                return False

            first_match = s_pointer < len(s) and  p[p_pointer] in {s[s_pointer],'.'}

            if p_pointer+1 < len(p) and p[p_pointer+1] == '*':
                return (check(s_pointer,p_pointer+2) or 
                    first_match and check(s_pointer+1,p_pointer))
            
            return check(s_pointer+1,p_pointer+1) and first_match
 
        return check(0,0)