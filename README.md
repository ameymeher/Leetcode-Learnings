# Leetcode-Learnings
Essential learning from Leetcode problems

| # | Summary | Comments | References |
|---|---------|----------|------------|
| 1 | Efficient operations based on if input from a stream or a list | - Better to do sort on the complete list <br> - If possible do bucket sort for input from a stream <br> - Basically, see how you can optimize for these two scenarios | [Minimum Time Difference - Bucket Sort](Algorithms/Minimum%20Time%20Difference%20-%20Bucket%20Sort.py) |
| 2 | If the size of a data structure is fixed, consider array too instead of using a general data structure | - Had to implement a Deque with fixed size <br> I choose the data structure as a double ended linked list <br> - It was correct, but since the size is fixed, can also use an array <br> - Keep an eye out for a simple solution rather than a general one | [Circular Deque](./Data%20Structures/Circular%20Deque.py) | 
| 3 | Rain water problems mostly can be solved with Two pointers | - I solved it using monotonic stack, which was also good <br> - There was a two pointer solution which was more amazing | 1. [Trapping Rain Water](./Two%20Pointers/Trapping%20Rain%20Water.py) <br>2. [Trapping Rain Water - Monotonic Stack](./Monotonic%20Stack/Trapping%20Rain%20Water.py) |