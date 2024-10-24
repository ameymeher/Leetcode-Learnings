class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        """
        1. Handling the unary operator was a task, that needed to be done at the closing bracket
        """
        op_stack = [] #[]
        curr_op = None #!
        val = None #False

        op_map = {
            '&' : lambda x,y: x&y,
            '|' : lambda x,y: x|y,
            '!' : lambda x: not x
        }

        for c in expression:
            if c in set('&|!'):
                if curr_op is not None:
                    op_stack.append(curr_op)
                    op_stack.append(val)
                curr_op = c
                val = None

            elif c in set('ft'):
                if val is None:
                    val = True if c == 't' else False
                else:
                    val = op_map[curr_op](val,True if c == 't' else False)

            elif c == ')':
                if curr_op == '!':
                    val =  not val

                if not op_stack:
                    return val
                else:
                    prev_val = op_stack.pop()
                    curr_op = op_stack.pop()
                    if prev_val is not None:
                        val = op_map[curr_op](val,prev_val)

        return val

"""
curr_op = &
prev_val = F
val = F
[&,F]
"""

