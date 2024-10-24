"""
1. Adding the first one seperately when binary operators are there
2. Then applying the operators for further numbers
3. Discarding the numbers starting with 0
"""

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        ans = []

        def backtrack(curr_i,expr,value,last):
            nonlocal target, num

            if curr_i == len(num):
                if value == target:
                    ans.append(expr)
                    return

            for i in range(curr_i+1,len(num)+1):
                new_value = num[curr_i:i]

                if new_value[0] == '0' and i - curr_i > 1:
                    break
                
                if curr_i == 0:
                    backtrack(i,new_value,int(new_value),int(new_value))
                else:
                    backtrack(i,
                        expr + '+' + new_value,
                        value + int(new_value),
                        int(new_value))

                    backtrack(i,
                        expr + '-' + new_value,
                        value - int(new_value),
                        -int(new_value))

                    backtrack(i,
                        expr + '*' + new_value,
                        value - last + last * int(new_value),
                        last*int(new_value))

        backtrack(0,'',0,0)

        return ans
