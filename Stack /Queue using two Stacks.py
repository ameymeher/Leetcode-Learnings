"""
Implement a queue using two stacks.
"""

queue_stack = []
aux_stack = []

def enqueue(val):
    queue_stack.append(val)
    
def dequeue():
    if not queue_stack and not aux_stack:
        return None
                
    if not aux_stack:
        while queue_stack:
            aux_stack.append(queue_stack.pop())
        
    return aux_stack.pop()
    
q = int(input())
for i in range(q):
    ins = input().split()

    if ins[0] == '1':
        enqueue(int(ins[1]))

    elif ins[0] == '2':
        dequeue()
    else:            
        if not aux_stack:
            if queue_stack:
                print(queue_stack[0])
        else:
            print(aux_stack[-1])
    
