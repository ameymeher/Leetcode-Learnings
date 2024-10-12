"""
You're trying to open a lock. The lock comes with a wheel which has the integers from 1 to 
N arranged in a circle in order around it (with integers 1 and N adjacent to one another). 
The wheel is initially pointing at 1.

It takes 1 second to rotate the wheel by 1 unit to an adjacent integer in either direction, 
and it takes no time to select an integer once the wheel is pointing at it.
The lock will open if you enter a certain code. The code consists of a sequence of M integers, the ith of which is Ci
Determine the minimum number of seconds required to select all M of the code's integers in order.

1. % operator behavior is having the same sign as the divisor.
2. Therefore, we can use this to calculate the minimum distance between two numbers.
"""


from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  
  pos = 1
  time = 0
  for i in C:
    time += min((pos-i)%N,(i-pos)%N)
    pos = i
    
  return time