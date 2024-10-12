"""
A cafeteria table consists of a row of N seats, numbered from 1 to N from left to right. 
Social distancing guidelines require that every diner be seated such that K seats to their left and K seats to their right (or all the remaining seats to that side if there are fewer than K) remain empty.

There are currently M diners seated at the table, the ith of whom is in seat Si
 
No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.
Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
Please take care to write a solution which runs within the time limit.
"""

from typing import List

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  S.sort()
  prev = 1
  ans = 0
  
  for i,curr in enumerate(S):
    if i == 0:
      ans += (curr - prev)//(K+1)
    else:
      ans += (curr - prev - 1 - K)//(K+1)
      
    prev = curr
  ans += (N-prev)//(K+1)
  return ans

print(getMaxAdditionalDinersCount(15,2,3,[11,6,14]))
