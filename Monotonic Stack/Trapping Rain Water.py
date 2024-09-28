class Solution:
    def trap(self, height: List[int]) -> int:
        
        stack = []

        ans = 0
        for i,h in enumerate(height):
            if not stack or stack[-1][0] > h:
                stack.append((h,i))
            else:
                prev_h = 0
                while stack and stack[-1][0] <= h:
                    stack_h,stack_i = stack.pop()
                    ans += (i-stack_i-1)*(stack_h-prev_h)
                    prev_h = stack_h
                
                if stack:
                    ans+=(i-stack[-1][1]-1)*(h-prev_h)

                stack.append((h,i))

        return ans

"""
        [0,1,0,2,1,0,1,3,2,1,2,1]


        (1-0-1) * 0
        (3-1-1) * 1 = 1
        (6-4-1) * 1 = 1
        (7-3-1) * 1 = 3
        (10-8-1) * 1 = 1


        (1,11)
        (2,10)
        (3,7)


        [4,2,0,3,2,5]

        prev = 3

        (3-1-1) * min(2-0,3) = 2
        (3-0-1) * min(3-2,)
        (5-3-1) * min(3-2,5) = 1
        (5-0-1) * min(4-3,5) = 4

        (5,5)


"""






