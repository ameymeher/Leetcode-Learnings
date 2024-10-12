"""
There are two types of operations possible
(0,a,b) - Save a rectangle of dimensions a*b
(1,a,b) - Check if a rectangle of dimensions a*b can be fit inside the saved rectangles. We can rotate the rectangle if necessary
"""

def rectangleFit(n, operations):
    # Write your code here
    rectangles = []
    for i in range(n):
        op, a, b = operations[i]
        if op == 0:
            rectangles.append((a, b))
        else:
            a, b = sorted([a, b])
            for x, y in rectangles:
                if x >= a and y >= b:
                    print("YES")
                    break
            else:
                print("NO")