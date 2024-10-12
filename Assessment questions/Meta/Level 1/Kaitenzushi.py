"""
There are N dishes in a row on a kaiten belt, with the ith dish being of type Di
Some dishes may be of the same type as one another.
You're very hungry, but you'd also like to keep things interesting. 
The N dishes will arrive in front of you, one after another in order, and for each one you'll eat it as long as it isn't the same type as any of the previous K dishes you've eaten. You eat very fast, so you can consume a dish before the next one gets to you. 
Any dishes you choose not to eat as they pass will be eaten by others.
Determine how many dishes you'll end up eating.
Please take care to write a solution which runs within the time limit.

1. I made a mistake here by thinking that I have to keep track of the last K dishes.
2. I just have to keep track of the last K dishes EATEN.
3. Instead of maintaining a HashMap, I can just maintain a set.
4. With a HashMap, I was maintaining the dishes even if they were not eaten
5. With a set, I am maintaining the dishes that were eaten.
6. Read the question properly therefore and check the operation on sample input first.
"""

from typing import List
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
  from collections import Counter,deque
  
  last_dishes = set()
  order = deque()
  
  ans = 0
  
  for dish in D:
    if dish not in last_dishes:
      ans +=1
      last_dishes.add(dish)
      order.append(dish)
    
      if len(last_dishes) > K:
        last_dishes.remove(order.popleft())
      
  return ans