"""
Assumptions:
1. Returning an array of length of functions that are executed
2. Return the exclusive time
3. For the recursive variant, the function id would be different? No
4. n = number of functions
5. op as 'start' and 'end' in strings

Edge case:
1. 1 2time 

Stack solution to store the latest program executed
1. When the current is start, update the time for the last one and push this on the stack
2. When the current is enf, update the time for the current one and pop from the stack
"""

def get_exclusive_time(n,arr):

    stack = [] # O(N) space 
    ans = [0]*n # O(N) space
    prev = 0

    for log in arr: #O(N) time
        l = log.split(':')
        p_id = int(l[0])
        op = l[1]
        time = int(l[2])

        if op == 'start':
            if stack:
                ans[stack[-1]]+=time-prev
            stack.append(p_id)
            prev = time
        else:
            if stack:
                ans[stack[-1]]+=time-prev+1
            stack.pop()
            prev=time+1
    
    return ans

"""
n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

stack = []
ans = [3,4]
prev = 6

Time: O(N) for iterating the log
Space: O(N) for stack
"""